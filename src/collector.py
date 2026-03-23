from psutil import cpu_percent, virtual_memory, disk_partitions,disk_usage

def getCpuPercent():
    stats = cpu_percent(interval=0.5,percpu=True) #returns the full list of each CPU/core (in my case, 20)
    whole = str(int(sum(stats)/len(stats))) #returns the average (like the windows task manager)
    return [int(whole),stats]

def getRAM():
    return [(virtual_memory())[i] for i in (0,2,3)] #returns total, percentage and used in a list. Note it includes the pagefile (swap), for me it's 1.1GB thus upping the total..

def getDisk():
    partitions_list = disk_partitions() 
    partitions = [partition[1] for partition in partitions_list] #The list of mounted partition letters [C:\,D:\...]."running over" the former partitions to save on creating new variables.
    results = {}
    for i in range(len(partitions)):
        results[partitions_list[i][0]] = disk_usage(partitions[i])
    
    return results

def getParitionsLetters():
    partitions_list = disk_partitions() 
    partitions = [partition[1][:2] for partition in partitions_list] # [1] to get the parition names, [:2] to cut the "://"
    return partitions



# RAM and DISK not passed as str like the CPU in order to be able to interact with the numbers later on.