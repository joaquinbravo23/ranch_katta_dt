class ProductDemand:
    def __init__(self, id_sku, quantity, price):
        self.id_sku = id_sku
        self.quantity = quantity
        self.price = price

    def __repr__(self):
        """Return a string representation of the product demand."""
        return f"SKU: {self.id_sku}, Quantity: {self.quantity}, Price: {self.price}"