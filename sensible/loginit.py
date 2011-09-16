import logging
import os

#initialize logging

def create_env():
    """Sets logging level if LOGGING_DEBUG is set"""

    default_log_level = logging.INFO
    if os.environ.get("LOGGING_DEBUG") in ("1", "True", "on"):
        default_log_level = logging.DEBUG
    return default_log_level

class Formatter(object):
    """A core log formatter"""

    def console_formatter(self):
        """Console Formatter"""
        format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        console_format = logging.Formatter(format)
        return console_format

def initialize_handlers():
    """Initializes Handlers"""

    default_log_level = create_env()
    handlers = []
    formatter = Formatter()

    #setup console handler
    console = logging.StreamHandler()
    console.setFormatter(formatter.console_formatter())
    console.setLevel(default_log_level)
    handlers.append(console)
    return handlers

_log = None
def logger(name, handlers=initialize_handlers):
    """Initializes Logging"""

    global _log
    if _log is not None:
        return _log
    else:
        log = logging.getLogger(name)
        log.setLevel(logging.DEBUG)
        for handler in handlers():
            log.addHandler(handler)
        return log