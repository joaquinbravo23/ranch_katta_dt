from datetime import datetime, timedelta

class ProductSetup:
    def __init__(self, id_product : str, setup_time : timedelta, start_date = datetime.min):
        self.id_product = id_product
        self.setup_time = setup_time
        self.start_date = start_date
        self.end_date = start_date + setup_time

    def __repr__(self):
        """Return a string representation of the product setup."""
        if self.start_date == datetime.min:
            return f"Setup(Product: {self.id_product}, Setup Time: {self.setup_time} hours)"
        else:
            return (f"Setup(Product: {self.id_product}, Setup Time: {self.setup_time} hours, "
                    f"Start: {self.start_date}, End: {self.end_date})")