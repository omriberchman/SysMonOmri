import collector,logger,display
import time

refreshTime = 1
originalPartitionList = collector.getParitionsLetters()

display.start()
try:
    while True:
        information = {"CPU":collector.getCpuPercent(),
               "RAM":collector.getRAM(),
               "DISK":collector.getDisk()
               } 
        display.update(information)
        logger.init(information)
        logger.printToLog(originalPartitionList, collector.getParitionsLetters())
        time.sleep(refreshTime)

except KeyboardInterrupt:
    display.stop()
    logger.NukeFile()
    print("Shutting down...")