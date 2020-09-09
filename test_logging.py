#!/usr/bin/env python

import logging

logger = logging.getLogger('ilogger')
logger.setLevel(logging.DEBUG)

sh = logging.StreamHandler(stream=None)
fh = logging.FileHandler(filename='ilog.log', mode='w')

# create formatter
fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s"
datefmt = "%a %d %b %Y %H:%M:%S"
formatter = logging.Formatter(fmt, datefmt)

sh.setFormatter(formatter)
fh.setFormatter(formatter)

sh.setLevel(level=logging.WARNING)
fh.setLevel(level=logging.INFO)

logger.addHandler(sh)
logger.addHandler(fh)

logger.critical('critical log')
logger.error('error log')
logger.warning('warning log')
logger.info('info log')
logger.debug('debug log')
