import collector,logger,display
import time
import argparse



parser = argparse.ArgumentParser()
parser.add_argument(
    "--interval",
    type=int,
    default=1,
    required=False,   #because the default is 1
    help="Time to check"
)
parser.add_argument(
    "--log",
    type=str,
    required=False,
    default="..\log.csv", 
    help="Custom location of the log file"
)
parser.add_argument(
    "--cpu-warn",
    type=int,
    required=False,
    default=95, 
    help="CPU warning above %"
)
parser.add_argument(
    "--mem-warn",
    type=int,
    required=False,
    default=95, 
    help="RAM warning above %"
)
args = parser.parse_args()

display.cpu_warn == args
logger.log_location = args.log
refreshTime = args.interval
originalPartitionList = collector.getParitionsLetters()

display.start(refreshTime)
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