from datetime import datetime, timedelta

class Task:
    def __init__(self, id_product: str, amount: int, amount_asked: int, machine: str, start_date: datetime, duration: timedelta):
        self.id_product = id_product
        self.amount = amount
        self.amount_asked = amount_asked
        self.machine = machine
        self.start_date = start_date
        self.duration = duration
        self.end_date = start_date + duration

    def __eq__(self, other):
        if isinstance(other, Task):
            return (self.id_product == other.id_product and
                    self.amount == other.amount and
                    self.amount_asked == other.amount_asked and
                    self.machine == other.machine and
                    self.start_date == other.start_date and
                    self.duration == other.duration)
        return False

    def __repr__(self):
        return (f"Task(Product: {self.id_product}, Amount Asked: {self.amount_asked}, "
                f"Amount Able: {self.amount}, Machine: {self.machine}, "
                f"Start: {self.start_date}, End: {self.end_date})")