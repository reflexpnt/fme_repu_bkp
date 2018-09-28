import logging, threading, functools
import time

logging.basicConfig(level=logging.NOTSET,
                    format='%(threadName)s %(message)s')

class PeriodicTimer(object):
    def __init__(self, interval, callback):
        self.interval = interval

        @functools.wraps(callback)
        def wrapper(*args, **kwargs):
            result = callback(*args, **kwargs)
            if result:
                self.thread = threading.Timer(self.interval,
                                              self.callback)
                self.thread.start()

        self.callback = wrapper

    def start(self):
        self.thread = threading.Timer(self.interval, self.callback)
        self.thread.start()

    def cancel(self):
        self.thread.cancel()


def foo():
    logging.info('Doing some work...')
    return True

timer = PeriodicTimer(5, foo)
timer.start()

for i in range(2):
    time.sleep(2)
    logging.info('Doing some other work...')

timer.cancel()