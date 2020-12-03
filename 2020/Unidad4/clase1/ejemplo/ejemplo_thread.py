import time

from threading import Thread


class Hilo1(Thread):
    def __init__(self, i):
        Thread.__init__(self)
        self.i = i

    def run(self):
        print (f"thread {self.i} sleeps for 5 seconds")
        time.sleep(5)
        print (f"thread {self.i} woke up")

    def start(self):
        yield self.run()
