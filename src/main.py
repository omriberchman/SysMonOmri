from rich.live import Live
from rich.table import Table
import time
import collector

refreshInterval = 2


with Live(refresh_per_second=1) as live:
    while True:
        table = Table(title="System Metrics")
        table.add_column("Metric")
        table.add_column("Value")
        table.add_row("CPU",f"{collector.getCpuPercent()[0]}%") # ==> CPU O% 
        # ... populate with data from collector ...
        live.update(table)
        time.sleep(refreshInterval)



# stats = psutil.cpu_percent(interval=0.9,percpu=True)
# print(len(stats))
# print(sum(stats)/len(stats))