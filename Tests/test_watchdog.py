import unittest
import multiprocessing
import time
from Services.Watchdog import watchdog

class TestWatchdog(unittest.TestCase):


    def test_watchdog_with_invalid_timeout(self):
        terminate_event = multiprocessing.Event()
        timeout = "neplatný timeout"
        with self.assertRaises(ValueError):
            watchdog(timeout, terminate_event)

if __name__ == '__main__':
    unittest.main()
