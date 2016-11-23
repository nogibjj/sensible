[![Build Status](https://travis-ci.org/nogibjj/sensible.svg?branch=master)](https://travis-ci.org/nogibjj/sensible)

#A "Sensible" Logging Configuration For Python.

##Example

    >>> from sensible.loginit
    import logger
    >>> log = logger("MyApp")
    >>> log.info("stuff")
    2009-08-04 23:56:22,583 - MyApp - INFO - stuff

##Easy to Toggle Debug Logging

If you want to print log.debug messages, set the environmental variable:

    LOGGING_DEBUG = 1

##Additional Features

Eliminates duplicate logging message by stopping log propogation.

###Advanced example [see examples directory](https://github.com/nogibjj/sensible/tree/master/examples) (logging via commandline daemon using click framework)

 ```bash
    pip install -r requirements.txt
    ➜  examples git:(master) ✗ python worker.py start && tail -f *.log
Starting worker.py ... OK
2016-11-22 17:32:56,739 - __main__ - INFO - START DAEMON
2016-11-22 17:32:56,740 - __main__ - INFO - EXECUTING WORK LOOP #[1]


 ```

https://github.com/nogibjj/sensible/blob/master/examples/README.md
