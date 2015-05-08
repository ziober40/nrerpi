__author__ = 'Bartek'

from delaychecker import CheckDelay
from apscheduler.schedulers.blocking import BlockingScheduler


sched = BlockingScheduler()


@sched.scheduled_job('interval', seconds=30)
def timed_job():
    checkdelay = CheckDelay()
    delayed_trains = checkdelay.get_delayed_trains()
    if len(delayed_trains) != 0:
        print("following trains are delayed")
        for dt in delayed_trains:
            print(dt)
    else:
        print("no delays")


sched.start()