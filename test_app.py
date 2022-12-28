from flask import Flask
from  small import app

import logging
import unittest

class TestLogConfiguration(unittest.TestCase):
    """[config set up]
    """
    def test_INFO__level_log(self):
        """
        Verify log for INFO level
        """
        self.app = app
        self.client = self.app.test_client

        with self.assertLogs() as log:
            user_logs = self.client().get('/')
            self.assertEqual(len(log.output), 4)
            self.assertEqual(len(log.records), 4)
            self.assertIn('ric flair', log.output[0])
    
    def test_WARNING__level_log(self):
      """
      Verify log for WARNING level
      """
      self.app = app
      self.client = self.app.test_client

      with self.assertLogs() as log:
          user_logs = self.client().get('/')
          self.assertEqual(len(log.output), 4)
          self.assertIn('disk', log.output[1])

