from datetime import datetime, timedelta
from setup import ProductSetup
from machine import GlassMaker
from product import Product
from task import Task
from demand import ProductDemand 

if __name__ == "__main__":
    products = [
        Product("GlassA", "GlassA", 100, "gr", 10.00, 100, 90),
        Product("GlassB", "GlassB", 200, "gr", 10.00, 80, 120),
        Product("GlassC", "GlassC", 300, "gr", 20.00, 50, 60),
    ]

    demands = [
        ProductDemand("GlassA", 300, 20.00),
        ProductDemand("GlassB", 300, 30.00),
        ProductDemand("GlassC", 300, 50.00),
    ]
    setup_times = [
        ProductSetup("GlassA", timedelta(minutes=30)),
        ProductSetup("GlassB", timedelta(minutes=20)),
        ProductSetup("GlassC", timedelta(minutes=25)),
    ]

    gm = GlassMaker(num_machines=2, products=products, demands=demands, setup_times=setup_times)

    tasks = [
        Task("GlassA", 10, 10, None, datetime(2023, 6, 1, 8, 0), timedelta(hours=2)),
        Task("GlassB", 5, 5, None, datetime(2023, 6, 1, 10, 0), timedelta(hours=1)),
        Task("GlassC", 7, 7, None, datetime(2023, 6, 1, 12, 0), timedelta(hours=1.5)),
    ]
    print(gm.automated_scheduling(tasks))