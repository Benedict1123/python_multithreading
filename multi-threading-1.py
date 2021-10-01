import threading
import time
from time import gmtime, strftime
start = time.perf_counter()


def take_action():
    print(f'Sleeping for 1 second...and now it is {strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())}/')
    time.sleep(1)
    print(f'Wake up after sleeping...and now it is {strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())}/')


thread_1 = threading.Thread(target=take_action)  # just pass in the function itself, un-executed
thread_2 = threading.Thread(target=take_action)

thread_1.start()
thread_2.start()
thread_1.join()  # add the thread to the main thread
thread_2.join()


finish = time.perf_counter()

print(f'Finished in {round(finish-start,2)} second(s)')

