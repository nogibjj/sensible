#!/usr/bin/env python
"""Startup Daemon Worker

Documentation:

Example of a more complex use of sensible logging

Daemon From Library  https://pypi.python.org/pypi/daemonocle


"""

import logging.handlers
import datetime
import time
import click
from daemonocle.cli import DaemonCLI
from sensible.loginit import logger

#Setup log formatter for sensible
from sensible.loginit import Formatter
formatter = Formatter()

#SETUP File Logging as Well
TODAY = datetime.datetime.now().strftime("%Y-%m-%d")
LOG_FILENAME = "%s.log" % TODAY
log = logger(__name__)
file_handler = logging.handlers.RotatingFileHandler(
              LOG_FILENAME, maxBytes=1000000, backupCount=5)
file_handler.setFormatter(formatter.console_formatter())
log.addHandler(file_handler)

@click.command(cls=DaemonCLI, 
    daemon_params={'pidfile': '/mmi/data/mworker.pid'})
def main(interval=10):
    """Boilerplate Daemon"""
    
    count = 0
    log.info("START DAEMON")
    while True:
        count +=1
        work_msg = "EXECUTING WORK LOOP #[%s]" % count
        log.info(work_msg)
        time.sleep(interval)
        loop_msg = "POLLING IN [%s]" % interval
        log.info(loop_msg)

if __name__ == '__main__':
    main()