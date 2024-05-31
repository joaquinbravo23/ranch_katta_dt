from datetime import timedelta

class ProductSetup:
    def __init__(self, id_sku : str, setup_time : timedelta):
        self.id_sku = id_sku
        self.setup_time = setup_time

    def __repr__(self):
        """Return a string representation of the product setup."""
        return f"SKU ID: {self.id_sku}, Setup Time: {self.setup_time} hours"