from typing import List, Optional, Dict, Tuple
from datetime import datetime, timedelta
from setup import ProductSetup
from product import Product
from task import Task
from demand import ProductDemand

class GlassMaker:
    def __init__(self, num_machines: int, products : List[Product], demands : List[ProductDemand], setup_times: List[ProductSetup]):
        self.schedules: List[List[Task]] = [[] for _ in range(num_machines)]
        self.setup_times = setup_times
        self.num_machines = num_machines

    def can_insert(self, machine_schedule: List[Task], new_task: Task) -> bool:
        for task in machine_schedule:
            if not (new_task.end_date <= task.start_date or new_task.start_date >= task.end_date):
                return False
        return True

    def calculate_setup_time(self, machine_schedule: List[Task], new_task: Task) -> timedelta:
        if not machine_schedule:
            return timedelta(0)
        last_task = machine_schedule[-1]
        if last_task.id_product != new_task.id_product:
            return next((setup.setup_time for setup in self.setup_times if setup.id_sku == new_task.id_product), timedelta(0))
        return timedelta(0)

    def insert_task(self, amount_asked: int, product: str, machine: Optional[int], start_date: datetime, duration: timedelta) -> str:
        new_task = Task(product, amount_asked, amount_asked, machine, start_date, duration)
        best_machine = None
        best_start_time = None
        min_end_time = datetime.max

        for i, machine_schedule in enumerate(self.schedules):
            print(i,'HOLA')
            setup_time = self.calculate_setup_time(machine_schedule, new_task)
            new_task.start_date = start_date + setup_time
            new_task.end_date = new_task.start_date + duration

            if self.can_insert(machine_schedule, new_task):
                if new_task.end_date < min_end_time:
                    best_machine = i
                    best_start_time = new_task.start_date
                    min_end_time = new_task.end_date

        if best_machine is not None:
            new_task.machine = best_machine
            new_task.start_date = best_start_time
            new_task.end_date = best_start_time + duration

            if setup_time != timedelta(0):
                self.schedules[best_machine].append(ProductSetup(product, setup_time))

            self.schedules[best_machine].append(new_task)
            # self.schedules[best_machine].sort(key=lambda event: event.start_date)
            return self.get_schedule()
        else:
            return "Task cannot be inserted due to a scheduling conflict."

    def delete_task(self, amount_asked: int, product: str, machine: int) -> str:
        for task in self.schedules[machine]:
            if task.amount_asked == amount_asked and task.product == product:
                self.schedules[machine].remove(task)
                return self.get_schedule()
        return "Task not found."

    def automated_scheduling(self, tasks: List[Task]) -> str:
        tasks.sort(key=lambda task: task.start_date)
        self.schedules = [[] for _ in range(self.num_machines)]
        for task in tasks:
            result = self.insert_task(task.amount_asked, task.id_product, None, task.start_date, task.duration)
            if "Task cannot be inserted" in result:
                return "Automated scheduling failed due to a conflict."
        return self.get_schedule()

    def get_schedule(self) -> str:
        schedule_output = []
        for i, machine_schedule in enumerate(self.schedules):
            schedule_output.append(f"Machine {i}:")
            for event in machine_schedule:
                schedule_output.append(repr(event))
        return '\n'.join(schedule_output)
