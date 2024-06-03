from datetime import timedelta

class Product:
    def __init__(self, input_product_id: str, output_product_id: str, net_weight: float, weight_unit: str,
                 cost: float, production_rate: int, duration: int):
        self.output_product_id = output_product_id
        self.input_product_id = input_product_id
        self.net_weight = net_weight
        self.weight_unit = weight_unit
        self.cost = cost
        self.production_rate = production_rate
        self.duration = timedelta(minutes=duration)
        self._convert_weight_to_kg_if_necessary()

    def _convert_weight_to_kg_if_necessary(self):
        """Convert the net weight to kilograms if the weight unit is grams."""
        if self.weight_unit.lower() == 'gr':
            self.net_weight /= 1000
            self.weight_unit = 'kg'

    def __str__(self):
        """Return a string representation of the product."""
        return (f"Output Product ID: {self.output_product_id}, Input Product ID: {self.input_product_id}, "
                f"Net Weight: {self.net_weight} {self.weight_unit}, Cost: ${self.cost}, "
                f"Production Rate: {self.production_rate} units/hour, Duration: {self.duration}")
