import collector,logger,sysDisplay
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
    default="log.csv", 
    help="Custom location of the log file"
)
parser.add_argument(
    "--cpu-warn",
    action="store_true",
    help="Enable CPU warning"
)
parser.add_argument(
    "--mem-warn",
    action="store_true",
    help="Enable RAM warning"
)

args = parser.parse_args()
logger.log_location = args.log
refreshTime = args.interval
originalPartitionList = collector.getParitionsLetters()

display = sysDisplay.Display(interval=args.interval,cpu_warn_status=args.cpu_warn,mem_warn_status=args.mem_warn)
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