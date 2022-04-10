from logging import StreamHandler, FileHandler, Formatter
import logging
import sys
import os
import pytz

# setting time zone
jst_tz = pytz.timezone('Asia/Tokyo')


def init_logger(
        has_stream: bool,
        has_file: bool,
        logger_name='debug') -> logging.Logger:
    logger = logging.getLogger(logger_name)
    # handler check for avoid duplicate log
    has_handler: bool = len(logger.handlers) > 0
    if not has_handler:
        formatter = Formatter(fmt='%(asctime)s: %(message)s')
        logger.setLevel(logging.DEBUG)
        logger.propagate = False
        if has_stream:
            stream_handler = StreamHandler(sys.stdout)
            stream_handler.setFormatter(fmt=formatter)
            stream_handler.setLevel(logging.DEBUG)
            logger.addHandler(stream_handler)
        if has_file:
            path = create_log_file(path='./temp/{}.log'.format(logger_name))
            file_handler = FileHandler(filename=path)
            file_handler.setFormatter(fmt=formatter)
            file_handler.setLevel(logging.DEBUG)
            logger.addHandler(file_handler)
        logger.info('---logging start---')
    return logger


def create_log_file(path) -> None:
    has_log_file = os.path.exists(path)
    if not has_log_file:
        f = open(path, 'w')
        f.write('')
        f.close()
    return path
