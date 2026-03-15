import psutil


def getCpuPercent():
    stats = psutil.cpu_percent(interval=0.5,percpu=True) #returns the full list of each CPU/core (in my case, 20)
    whole = str(int(sum(stats)/len(stats))) #returns the average (like the windows task manager)
    return [str(int(whole)),stats]

def getRAM():
    return [(psutil.virtual_memory())[i] for i in (0,2,3)] #returns total, percentage and used in a list. Note it includes the page file (swap), for me it's 1.1GB thus upping the total..

def getDisk():
    return psutil.disk_usage("C:/")



print(getDisk()[0]/10**9)
# print(getRAM()[2]/(10**9)) #i'll use the bytes to GB convertion formula: number of bytes / 10^9 (number of bytes in a GB). Note that windows measures it in 1024**3 so it'll show a bit different than the task manager.