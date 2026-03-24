import csv
import time


class Logger():
    def __init__(self,passed_info):
        self.information = passed_info

    def update(self,passed_info):
        self.information = passed_info
        self.stats = [self.information['CPU'][0], self.information['CPU'][1],round(self.information['RAM'][0]/10**9,2),self.information['RAM'][1],round(self.information['RAM'][2]/10**9,2)]
        self.columns = ["CPUWhole", "CPUAllCores", "RAMTotal", "RAMPercentage", "RAMUsed"]
        self.log_location = 'log.csv' #..\ => the upper folder


        for key, value in self.information['DISK'].items():
            key = key[:1] #"C:/" == > "C" since partitions can only have 1 letter no issue..
            self.columns.append(str(key)+"Total")
            self.columns.append(str(key)+"Used")
            self.columns.append(str(key)+"Percent")
        #Add time parition:
        self.columns.append("Time")

        try:
            with open(self.log_location,'r') as log_file: #Checking if the file is empty (to add the first row as "title") or to skip that.
                if log_file.read(1): #file is empty
                    pass 
                else: #file already has content
                    with open(self.log_location, 'w', newline='') as log_file: 
                        writer = csv.writer(log_file)
                        writer.writerow(self.columns)
        except FileNotFoundError:
            with open(self.log_location, 'w', newline='') as log_file: 
                writer = csv.writer(log_file)
                writer.writerow(self.columns)
        for key in self.information['DISK'].values(): 
            self.stats.append(int(key[0]/10**9))
            self.stats.append(int(key[1]/10**9))
            self.stats.append(key[3])
        self.stats.append(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))


    def printToLog(self,fList,nList): #Fist list / New list (of partitions)
        if (fList > nList): #num_of_columns and not len(columns) because at time of declaration (if I declate outside of the init func) it only has the CPU and RAM ones.
            missing_partition = "" #the missing/unmounted partition
            for partition in fList:
                if partition not in nList:
                    missing_partition = partition
            num_to_skip = 0
            
            for i in range(len(fList)):
                if fList[i] > missing_partition:
                    num_to_skip = len(fList)-i
            
            index = -(num_to_skip*3+1) #Negative = from the end, num_to_skip*3 because of the 3 entries to each partition, +1 because of the 'Time' columns
            self.stats[index:index] = ["N/A", "N/A", "N/A"]

        with open(self.log_location,'a', newline='') as log_file: #a for append
            writer = csv.writer(log_file, )
            writer.writerow(self.stats)


    def NukeFile(self): #clear the log file
        if self.log_location.endswith(".csv"):
            with open(self.log_location, "w") as f:
                pass
        else:
            print("FILE PATH IS NOT A .CSV FILE NOT DELETING!!!")
