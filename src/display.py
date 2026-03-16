from rich.live import Live
from rich.table import Table
import time
import collector

refreshInterval = 2


with Live(refresh_per_second=1) as live:
    while True:
        information = {"CPU":collector.getCpuPercent(),"RAM":collector.getRAM(),"DISK":collector.getDisk()} #Dict, simpler than list, values in README.MD, done once to save on calling collector module multiple times
        # ^ also makes it easier to just kick the module collector from this module if needed and just pass the data through.
        
        CPUtable = Table(title="CPU Metrics")
        CPUtable.show_lines = True #Show lines between each value, easier to look.
        CPUtable.add_column("CPU")
        CPUtable.add_column("Value")
        CPUtable.add_row("Total",f"{information["CPU"][0]}%") # ==> Total | Z% 
        all_cores_display = ""
        for core in range(len(information["CPU"][1])):
            if core % 4 == 0:
                all_cores_display = (all_cores_display+"\n") # Go down every 4 core, for simplicity.
            else:
                all_cores_display = (all_cores_display+f" [{information["CPU"][1][core]}%] ") # Add core as "[Z%]"

        CPUtable.add_row("By core",f"{all_cores_display}") # ==> By core | [Z%] [Z%] [Z%] [Z%] ....

        RAMtable = Table(title="RAM Metrics")
        RAMtable.show_lines = True
        RAMtable.add_column("RAM")
        RAMtable.add_column("Value")
        RAMtable.add_row("Total", str(  round(  (information["RAM"][0])/(10**9) ,2)   )) #taking the ram 
        # RAMtable.add_row("Used", str(information["RAM"][2]/10^9))
        # RAMtable.add_row("  %  " , str(information["RAM"][1]))
        #Total,used, %

        live.update(CPUtable)
        live.update(RAMtable)
        time.sleep(refreshInterval)


# table.add_row("RAM",f"{information["RAM"][1]}%") # ==> RAM Z% 