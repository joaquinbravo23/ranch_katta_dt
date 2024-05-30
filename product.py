class Product:
    def __init__(self, output_product_id, input_product_id, output_product_description, 
                 product_classification, net_weight, weight_unit, cost):
        self.output_product_id = output_product_id
        self.input_product_id = input_product_id
        self.output_product_description = output_product_description
        self.product_classification = product_classification
        self.net_weight = net_weight
        self.weight_unit = weight_unit
        self.cost = cost
        self._convert_weight_to_kg_if_necessary()

    def _convert_weight_to_kg_if_necessary(self):
        """Convert the net weight to kilograms if the weight unit is grams."""
        if self.weight_unit.lower() == 'gr':
            self.net_weight /= 1000
            self.weight_unit = 'kg'

    def __str__(self):
        """Return a string representation of the product."""
        return (f"Output Product ID: {self.output_product_id}, Input Product ID: {self.input_product_id}, "
                f"Output Product Description: {self.output_product_description}, Product Classification: {self.product_classification}, "
                f"Net Weight: {self.net_weight} {self.weight_unit}, Cost: ${self.cost}")

# Example usage:
product = Product("OP123", "IP456", "High-quality steel bolts", "Hardware", 500, "gr", 250.00)
print(product)
