import os
import time

from threading import Thread, current_thread
from multiprocessing import Process, current_process

def play_sleep():
    pid = os.getpid()
    thread_name = current_thread().name
    process_name = current_process().name

    print(f"{pid} - {thread_name} - {process_name} - durmiendo")
    time.sleep(5)
    print(f"{pid} - {thread_name} - {process_name} - despertando")

def carga_cpu():
    pid = os.getpid()
    thread_name = current_thread().name
    process_name = current_process().name

    print(f"{pid} - {thread_name} - {process_name} - empieza a trabajar")
    n = 50000000
    while n > 0:
        n -= 1
    print(f"{pid} - {thread_name} - {process_name} - finaliza")

if __name__ == '__main__':
    start = time.time()
    # play_sleep()
    # play_sleep()
    # t1 = Thread(target=carga_cpu)
    # t2 = Thread(target=carga_cpu)
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()

    p1 = Process(target=carga_cpu)
    p2 = Process(target=carga_cpu)
    p1.start(); p2.start()
    p1.join(); p2.join()
    # carga_cpu()
    # carga_cpu()

    end = time.time()

    print(end-start)
