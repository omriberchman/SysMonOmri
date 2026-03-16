import csv
import collector

information= {"Disk":collector.getDisk()}
def init(passed_info):
    global information
    information = passed_info


columns = ["CPUWhole", "CPUAllCores", "RAMTotal", "RAMPercentage", "RAMUsed"] 
#Add partition columns:
for key, value in information['Disk'].items():
    key = key[:1] #"C:/" == > "C" since partitions can only have 1 letter no issue..
    columns.append(str(key)+"Total")
    columns.append(str(key)+"Used")
    columns.append(str(key)+"Percent")
    

print(columns)
with open('log.csv', mode='w') as log_file:
    writer = csv.writer(log_file)
    writer.writerow(columns)


# Not writing anything just yet, consider using this...

# information = {"CPU":getCpuPercent(),"RAM":getRAM(),"DISK":getDisk()}
# stats = [information['CPU'][0], information['CPU'][1],information['RAM'][0],information['RAM'][1],information['RAM'][2]]
# print(information)
# print(stats)
