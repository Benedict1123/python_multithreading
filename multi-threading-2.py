import threading
import time
from time import gmtime, strftime
start = time.perf_counter()


def take_action():
    print(f'Sleeping for 1 second...and now it is {strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())}/')
    time.sleep(1)
    print(f'Wake up after sleeping...and now it is {strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())}/')


threads = []

for _ in range(10):  # _ means a throwaway variable
    t = threading.Thread(target=take_action)  # just pass in the function itself, un-executed
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start,2)} second(s)')

