import unittest
import os
import logging

from loginit import initialize_handlers, logger, create_env

class TestLogInitSet(unittest.TestCase):

    def setUp(self):

        os.environ["LOGGING_DEBUG"] = "1"
        self.log_level = create_env()

    def test_env(self):

        assert self.log_level == logging.DEBUG

    def tearDown(self):

        del os.environ["LOGGING_DEBUG"]

class TestLogInitUnset(unittest.TestCase):

    def setUp(self):

        self.log_level = create_env()

    def test_unset_env(self):

        assert self.log_level == logging.INFO

    def tearDown(self):
        pass