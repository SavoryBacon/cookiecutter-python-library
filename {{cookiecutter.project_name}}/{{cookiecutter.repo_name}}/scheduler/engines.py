import logging
from apscheduler.schedulers.blocking import BlockingScheduler

logger = logging.getLogger(__name__.split('.')[0])

blocking_scheduler = BlockingScheduler(logger=logger)