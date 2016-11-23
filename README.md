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
