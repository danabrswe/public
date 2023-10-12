# thread        = a flow of execution. like a separate order of instructions.
#               However each thread takes a turn running to achieve concurrency
#               GIL = Global Interpreter Lock, allows only one thread to hold the control of the Python interpreter at any one time.

# cpu bound     = program/task spends most of its time waiting for internal events (CPU intensive)
#               --> use multipocessing

# io bound      = program/task spends most of its time waiting for external events (user input, web scraping)
#               --> use multithreading

import threading
import time

start_time = time.perf_counter() # start measuring performance time

def eat_breakfast():
    time.sleep(3)
    print("You ate breakfast")

def drink_coffee():
    time.sleep(4)
    print("You drank coffee")

def study():
    time.sleep(5)
    print("You studied")

x = threading.Thread(target=eat_breakfast,args=())
x.start()

y = threading.Thread(target=drink_coffee)
y.start()

z = threading.Thread(target=study)
z.start()

# main thread has to wait for other threads before continuing code execution
x.join()
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())        # prints list of all running thread. main thread is the thread running the main body of your program

end_time = time.perf_counter() # stop measuring time
print(round(elapsed_time := end_time - start_time, 4))  # print performance time of main thread
