__author__ = 'Bartek'

from delaychecker import CheckDelay
from apscheduler.schedulers.blocking import BlockingScheduler
from logger import Logger

import time

sched = BlockingScheduler()
logger = Logger()
logger.log("application started")


@sched.scheduled_job('interval', seconds=30)
def timed_job():
    checkdelay = CheckDelay()
    delayed_trains = checkdelay.get_delayed_trains()
    if len(delayed_trains) != 0:
        logger.log("following trains are delayed")
        for dt in delayed_trains:
            logger.log(dt)
    else:
        logger.log("no delays")


sched.start()
