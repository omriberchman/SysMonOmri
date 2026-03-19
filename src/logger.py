import csv
import time

information = {}
stats = []


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
        with open('log.csv','r') as log_file: #Checking if the file is empty (to add the first row as "title") or to skip that.
            if log_file.read(1): #file is empty
                pass 
            else: #file already has titles
                with open('log.csv', 'w', newline='') as log_file: 
                    writer = csv.writer(log_file)
                    writer.writerow(columns)
    except FileNotFoundError:
        with open('log.csv', 'w', newline='') as log_file: 
            writer = csv.writer(log_file)
            writer.writerow(columns)
    for key in information['DISK'].values(): 
        stats.append(int(key[0]/10**9))
        stats.append(int(key[1]/10**9))
        stats.append(key[3])
    stats.append(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))


def numOfColumns():
    with open('log.csv',"r") as log_file:
        number_of_words = log_file.readline().count(",")    
        return number_of_words+1 #Because the end of the line is an invisible char which is not typable


def printToLog():
    global stats
    print(f"~~~ {len(stats)} = {numOfColumns()} ~~~")
    if (len(stats) != numOfColumns()): #num_of_columns and not len(columns) because at time of declaration (if I declate outside of the init func) it only has the CPU and RAM ones.
        print("### OOPS NUMBER OF PARTIOTIONS CHANGED! ###")
    with open('log.csv','a', newline='') as log_file: #a for append
        writer = csv.writer(log_file, )
        writer.writerow(stats)


def NukeFile(): #clear the log file
    with open("log.csv", "w") as f:
        pass