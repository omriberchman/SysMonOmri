import csv
import time

information = {}
stats = []
log_location = 'log.csv' #..\ => the upper folder


def init(passed_info):
    global information
    information = passed_info
    global stats
    stats = [information['CPU'][0], information['CPU'][1],round(information['RAM'][0]/10**9,2),information['RAM'][1],round(information['RAM'][2]/10**9,2)]

    columns = ["CPUWhole", "CPUAllCores", "RAMTotal", "RAMPercentage", "RAMUsed"] 
    #Add partition columns:
    for key, value in information['DISK'].items():
        key = key[:1] #"C:/" == > "C" since partitions can only have 1 letter no issue..
        columns.append(str(key)+"Total")
        columns.append(str(key)+"Used")
        columns.append(str(key)+"Percent")
    #Add time parition:
    columns.append("Time")
    global num_of_columns

    try:
        with open(log_location,'r') as log_file: #Checking if the file is empty (to add the first row as "title") or to skip that.
            if log_file.read(1): #file is empty
                pass 
            else: #file already has content
                with open(log_location, 'w', newline='') as log_file: 
                    writer = csv.writer(log_file)
                    writer.writerow(columns)
    except FileNotFoundError:
        with open(log_location, 'w', newline='') as log_file: 
            writer = csv.writer(log_file)
            writer.writerow(columns)
    for key in information['DISK'].values(): 
        stats.append(int(key[0]/10**9))
        stats.append(int(key[1]/10**9))
        stats.append(key[3])
    stats.append(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))


def printToLog(fList,nList): #Fist list / New list (of partitions)
    global stats
       
    if (fList < nList): #num_of_columns and not len(columns) because at time of declaration (if I declate outside of the init func) it only has the CPU and RAM ones.

        missing_partition = "" #the missing/unmounted partition
        for partition in fList:
            if partition not in nList:
                missing_partition = partition
        num_to_skip = 0
        
        for i in range(len(fList)):
            if fList[i] > missing_partition:
                num_to_skip = len(fList)-i
        
        index = -(num_to_skip*3+1) #Negative = from the end, num_to_skip*3 because of the 3 entries to each partition, +1 because of the 'Time' columns
        stats[index:index] = ["N/A", "N/A", "N/A"]

            
    with open(log_location,'a', newline='') as log_file: #a for append
        writer = csv.writer(log_file, )
        writer.writerow(stats)


def NukeFile(): #clear the log file
    if log_location.endswith(".csv"):
        with open(log_location, "w") as f:
            pass
    else:
        print("FILE PATH IS NOT A .CSV FILE NOT DELETING!!!")
