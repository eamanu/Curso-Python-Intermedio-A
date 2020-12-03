import time

from threading import Thread
from subprocess import call


def worker():
    """
    i = 0
    while i < 50000000:
        i +=1
    """
    call(['python3', 'infinito.py'])


start = time.time()

# worker()

t = Thread(target=worker)
t2 = Thread(target=worker)
t.start(); t2.start()
t.join(); t2.join()

end = time.time()

print(end-start)
