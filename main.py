from datetime import datetime, timedelta
from setup import ProductSetup
from machine import GlassMaker
from task import Task

if __name__ == "__main__":
    setup_times = [
        ProductSetup("GlassA", timedelta(minutes=30)),
        ProductSetup("GlassB", timedelta(minutes=20)),
        ProductSetup("GlassC", timedelta(minutes=25)),
        ProductSetup("GlassD", timedelta(minutes=30)),
        ProductSetup("GlassE", timedelta(minutes=15)),
    ]

    gm = GlassMaker(num_machines=2, setup_times=setup_times)

    tasks = [
        Task("GlassC", 10, 10, None, datetime(2023, 6, 1, 8, 0), timedelta(hours=2)),
        Task("GlassD", 5, 5, None, datetime(2023, 6, 1, 8, 0), timedelta(hours=1)),
        Task("GlassE", 7, 7, None, datetime(2023, 6, 1, 10, 0), timedelta(hours=1.5)),
    ]
    print(gm.automated_scheduling(tasks))