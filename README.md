# SysMon project - Omri Berchman

### Written and tested in Python 3.10

## Why(s):
     

### <ins> In main.py variable 'Information' is a dict
Dict is simpler than list in this case, values can be found in README.MD, done once to save on calling collector module multiple times    
### <ins>RAM and Disk size appear different than window's task manager
 windows is calculating GBs as 1024^3, while most people (myself included) do it as 10^9.
### <ins>Information collected saperated into lists
I saperated the data I've collected in the collector module into lists: CPU, RAM and Disk. Here are the specs for each:    
* CPU : [0] = % of all cores, [1] = list of % of each core seperately.    
* RAM : [0] = Total (in bytes), [1] = % of RAM used, [2] = used (in bytes)
* Disk : ["n:\"][0] = Total of drive n (in bytes), ["n:\"][1] = Used ... (in bytes), ["n:\"][2] = Free ... (in bytes), ["n:\"][3] = percent, ["n+1:\"][1] = Total of drive n+1 and so on......    
### <ins> PermissionError when setting a custom log file location
You must add a file with .csv file ending not just a folder/path.    
### <ins>The '--interval' can't accept with value smaller than 1
The system will not accept value lower than 1, it doesn't work well with the sleep and psutil.Live combination..


## Features to be added 

### Colors
