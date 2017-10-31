import logging

logger = logging.getLogger(__name__.split('.')[0])

def sample_job(*args, **kwargs):
    print("sample_job ran")
    logger.info("sample_job ran")