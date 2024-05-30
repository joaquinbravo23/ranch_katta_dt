class ProductDemand:
    def __init__(self, id_sku, quantity, price):
        self.id_sku = id_sku
        self.quantity = quantity
        self.price = price

    def total_value(self):
        """Calculate the total value of the demand."""
        return self.quantity * self.price

    def __str__(self):
        """Return a string representation of the product demand."""
        return f"SKU: {self.id_sku}, Quantity: {self.quantity}, Price: {self.price}, Total Value: {self.total_value()}"

# Example usage:
demand = ProductDemand("Laptop", 10, 20)
print(demand)
print("Total value of demand:", demand.total_value())