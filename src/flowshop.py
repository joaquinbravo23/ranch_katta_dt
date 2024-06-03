from typing import List, Optional, Dict, Tuple
from datetime import datetime, timedelta
from product import Product
from task import Task
from setup import ProductSetup
from demand import ProductDemand
from machine import GlassMaker

class FlowShop:
    def __init__(self, products: Dict[str, Product], demands: Dict[str, ProductDemand], machines: Dict[str, GlassMaker]):
        self.products = products
        self.demands = demands
        self.machines = machines
        self.profit = 0

    def insert_task(self, id_product: str, amount: int, amount_asked: int) -> bool:
        for product in self.products.values():
            if product.output_product_id == id_product:
                duration = product.duration
                start_date = datetime.min
                machine = ""
                break
        new_task = Task(id_product, amount, amount_asked, machine, start_date, duration)

        for machine in self.machines.values():
            net_weight = product.net_weight
            production_rate = product.production_rate

            if machine.melted_glass < net_weight*production_rate:
                if machine.schedule:
                    melt_setup_time = machine.setup_times["MeltedGlass"].setup_time
                    machine.schedule.append(ProductSetup("MeltedGlass", melt_setup_time, machine.actual_date))
                    machine.actual_date += melt_setup_time
                
                machine.melt_glass(self.products["MeltedGlass"])
                melt_duration = self.products["MeltedGlass"].duration
                melt_task = Task("MeltedGlass", 1, 1, machine.id_machine, machine.actual_date, melt_duration)
                machine.schedule.append(melt_task)
                machine.actual_date += melt_duration
                self.profit -= self.products["MeltedGlass"].cost
            
            setup_time = machine.calculate_setup_time(new_task)
            new_task.start_date = machine.actual_date + setup_time
            new_task.end_date = new_task.start_date + duration

            if machine.can_insert(new_task):                
                if setup_time != timedelta(0):
                    machine.schedule.append(ProductSetup(id_product, setup_time, machine.actual_date))
                new_task.machine = machine.id_machine
                machine.schedule.append(new_task)
                machine.actual_date = new_task.end_date
                machine.melted_glass -= net_weight*production_rate
                self.profit += amount * (self.demands[id_product].price - self.products[id_product].cost)
                return True
        return False

    def delete_task(self, id_product :str) -> bool:
        delete = False
        for machine in self.machines.values():
            last_task = machine.schedule[-1]
            if machine.schedule and last_task.id_product == id_product:
                machine.schedule.remove(last_task)
                if isinstance(last_task, Task):
                    if id_product == "MeltedGlass":
                        self.profit += self.products[id_product].cost
                    else:
                        self.profit -= last_task.amount * (self.demands[id_product].price - self.products[id_product].cost)
                delete = True
        return delete
        
    def automated_scheduling(self) -> str:
        insert, remove = True, True
        while insert:
            filtered_demands = {k: v for k, v in self.demands.items() if v.quantity != 0}
            demand = max(filtered_demands, key=lambda k: filtered_demands[k].price, default=None)
            if demand != None:
                production_rate = self.products[demand].production_rate
                amount_asked = self.demands[demand].quantity
                amount = min(production_rate, amount_asked)
                insert = self.insert_task(demand, amount, amount_asked)
                if insert:
                    self.demands[demand].quantity -= amount
            else:
                insert = False

        while remove:
            remove = self.delete_task("MeltedGlass")
                
        return self.get_schedule()

    def get_schedule(self) -> str:
        schedule_output = []
        for machine in self.machines.values():
            schedule_output.append(f"Machine {machine.id_machine}:")
            for event in machine.schedule:
                schedule_output.append(repr(event))
        schedule_output.append(f"Profit: {self.profit}")
        return '\n'.join(schedule_output)
