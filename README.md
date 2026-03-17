# SysMon project - Omri Berchman

### Written and tested in Python 3.10

## Why(s):
     
### RAM and Disk size appear different than window's task manager
 windows is calculating GBs as 1024^3, while most people (myself included) do it as 10^9.

### Information collected saperated into lists
I saperated the data I've collected in the collector module into lists: CPU, RAM and Disk. Here are the specs for each:    
* CPU : [0] = % of all cores, [1] = list of % of each core seperately.    
* RAM : [0] = Total (in bytes), [1] = % of RAM used, [2] = used (in bytes)
* Disk : ["n:\"][0] = Total of drive n (in bytes), ["n:\"][1] = Used ... (in bytes), ["n:\"][2] = Free ... (in bytes), ["n:\"][3] = percent, ["n+1:\"][1] = Total of drive n+1 and so on......


## Features to be added 
### Graph to the right of the "Value" coloumn:
Cool and makes readability easier.
### Colors
