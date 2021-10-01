import concurrent.futures
import time
from time import gmtime, strftime

start = time.perf_counter()


def take_action(duration_length):
    """Define a function to perform some actions
    :argument
    :return: an ending information showing that the actions has been executed
    """
    print(
        f'Sleeping for {duration_length} second(s)...and now it is {strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())}/')
    time.sleep(duration_length)
    return f'Wake up after sleeping...and now it is {strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())}/'


with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(take_action, 1)  # a scheduler
    f2 = executor.submit(take_action, 1)  # a scheduler
    print(f1.result())
    print(f2.result())

# threads = []
#
# for _ in range(10):  # _ means a throwaway variable
#     # just pass in the function itself, un-executed
#     t = threading.Thread(target=take_action, args=[2])  # args is a list of arguments to pass in
#     t.start()
#     threads.append(t)
#
# for thread in threads:
#     thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')
