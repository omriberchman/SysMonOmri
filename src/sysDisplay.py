from rich.live import Live
from rich.table import Table
from rich.columns import Columns #to display multiple tables at once
from notifypy import Notify 

class Display():
    def __init__(self,interval=1,cpu_warn_status=False, mem_warn_status=False):
        self.cpu_warn = cpu_warn_status
        self.mem_warn = mem_warn_status
        self.notification = Notify()
        self.live = Live(refresh_per_second=interval)
        self.live.start()

    def stop(self):
        if self.live:
            self.live.stop()

    def update(self,information):
        CPUtable = Table(title="CPU Metrics",style="green")
        CPUtable.show_lines = True #Show lines between each value, easier to look.
        CPUtable.add_column("CPU")
        CPUtable.add_column("Value")
        if (self.cpu_warn == True and information['CPU'][0] > 90):
            CPUtable.style = "red"
            self.notification.title = "CPU Warning"
            self.notification.message = "CPU capacity has reched over 90%"
            self.notification.send(block=False)
        CPUtable.add_row("Total",f"{information['CPU'][0]}%") # ==> Total | Z% 
        all_cores_display = ""
        for core in range(len(information['CPU'][1])):
            if core % 4 == 0:
                all_cores_display = (all_cores_display+"\n") # Go down every 4 core, for simplicity.
            else:
                all_cores_display = (all_cores_display+f" [{information['CPU'][1][core]}%] ") # Add core as "[Z%]"
        CPUtable.add_row("By core",f"{all_cores_display}") # ==> By core | [Z%] [Z%] [Z%] [Z%] ....
        
        RAMtable = Table(title="RAM Metrics",style="green")
        RAMtable.show_lines = True
        if (self.mem_warn == True and information['RAM'][1] > 90):
            RAMtable.style = "red"
            self.notification.title = "RAM Warning"
            self.notification.message = "RAM capacity has reached above 90%."
            self.notification.send(block=False)
        RAMtable.add_column("RAM")
        RAMtable.add_column("Value")
        RAMtable.add_row("Total", str(   round(  (information['RAM'][0])/(10**9) ,2)   )) #taking the getRAM() value from index 0, converts to GBs then rounds the decimal to 2. 
        RAMtable.add_row("Used", str(   round(information['RAM'][2]/10**9,2)))
        RAMtable.add_row("  %  " , str(    int(information['RAM'][1]))) #no need for decimal in %

        DiskTable = Table(title="Disk Metrics",style="green")
        DiskTable.show_lines = True
        DiskTable.add_column("Disk")
        DiskTable.add_column("Used")
        DiskTable.add_column("Total")
        DiskTable.add_column("  %  ")
        for key, value in information['DISK'].items(): #Print partition name and info
            DiskTable.add_row(str(key)    ,f"{str(  round(value[1]/10**9,0))}GB"    ,f"{str(  round(value[0]/10**9,0))}GB"    ,str(value[3])) #disk sizes in GBs, % is 3 because 2 is free space, a bit useless imo.

        self.live.update(Columns([CPUtable, RAMtable,DiskTable])) 