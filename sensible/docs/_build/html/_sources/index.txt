Sensible
====================================

Contents:

.. toctree::
   :maxdepth: 2

Author:  Noah Gift

Date:  08/05/2009

A really simple set of defaults for logging
============================================

You simply do this::

    >>> from sensible.loginit import logger
    >>> log = logger("MyApp")
    >>> log.info("stuff")
    2009-08-04 23:56:22,583 - MyApp - INFO - stuff

Environmental Variable
---------------------
If you want to print log.debug messages, you simply set
the environmental variable::

    export LOGGING_DEBUG = 1




Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

