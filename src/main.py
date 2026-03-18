import collector,logger,display
import time

refreshTime = 1

display.start()
try:
    while True:
        information = {"CPU":collector.getCpuPercent(),
               "RAM":collector.getRAM(),
               "DISK":collector.getDisk()
               } #Dict, simpler than list, values in README.MD, done once to save on calling collector module multiple times
        display.update(information)
        logger.init(information)
        logger.printToLog()
        time.sleep(refreshTime)

except KeyboardInterrupt:
    display.stop()
    logger.NukeFile()
    print("Shutting down...")