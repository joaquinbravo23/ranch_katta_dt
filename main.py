from datetime import datetime, timedelta
from setup import ProductSetup
from machine import GlassMaker
from product import Product
from demand import ProductDemand 
from machine import GlassMaker
from flowshop import FlowShop

if __name__ == "__main__":
    products = {
        "MeltedGlass" :Product("CrushedGlass", "MeltedGlass", 100, "kg", 1000.00, 1, 180),
        "GlassA" :Product("MeltedGlass", "GlassA", 100, "gr", 10.00, 200, 90),
        "GlassB" :Product("MeltedGlass", "GlassB", 200, "gr", 10.00, 300, 120),
        "GlassC" :Product("MeltedGlass", "GlassC", 300, "gr", 20.00, 200, 60),
    }

    demands = {
        "GlassA" :ProductDemand("GlassA", 500, 20.00),
        "GlassB" :ProductDemand("GlassB", 400, 30.00),
        "GlassC" :ProductDemand("GlassC", 300, 50.00),
    }

    setup_times = {        
        "MeltedGlass" :ProductSetup("MeltedGlass", timedelta(minutes=30)),
        "GlassA" :ProductSetup("GlassA", timedelta(minutes=20)),
        "GlassB" :ProductSetup("GlassB", timedelta(minutes=20)),
        "GlassC" :ProductSetup("GlassC", timedelta(minutes=25)),
    }
    
    machines = {
    "M01" :GlassMaker("M01", setup_times),
    "M02" :GlassMaker("M02", setup_times),
    }

    flowshop = FlowShop(products=products,
                        demands=demands,
                        machines=machines)
    
    print(flowshop.automated_scheduling())