from typing import List, Optional, Dict, Tuple
from datetime import datetime, timedelta
from setup import ProductSetup
from task import Task
from product import Product

class GlassMaker:
    def __init__(self, id_machine: str, setup_times: Dict[str, ProductSetup]):
        self.schedule: List[Task] = []
        self.id_machine = id_machine
        self.setup_times = setup_times
        self.start_date = datetime(2023, 6, 1, 6, 0)
        self.end_date = datetime(2023, 6, 1, 20, 0)
        self.actual_date = self.start_date
        self.melted_glass = 0

    def melt_glass(self, product : Product):
        net_weight = product.net_weight
        production_rate = product.production_rate
        self.melted_glass += net_weight*production_rate

    def calculate_setup_time(self, new_task: Task) -> timedelta:
        if self.schedule and self.schedule[-1].id_product != new_task.id_product:
            return next((setup.setup_time for setup in self.setup_times.values() if setup.id_product == new_task.id_product), timedelta(0))
        else: 
            return timedelta(0)

    def can_insert(self, new_task: Task) -> bool:  
        if self.actual_date < new_task.end_date < self.end_date:
            return True
        else:
            return False

