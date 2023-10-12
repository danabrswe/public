# daemon thread =   a thread that runs in the background. not important for program to run.
#                   Your program will not wait for daemon threads to complete before exiting.
#                   Non-daemon threads cannot normally be killed, they stay alive until task is complete.

#                   ex. background tasks, garbage collection, waiting for input, long-running processes

import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logged in for: ", count, " seconds")

x = threading.Thread(target=timer,daemon=True)
x.start()

# x.setDaemon(True)         # make thread into daemon thread. cannot be done while thread is active.

print(x.__getattribute__("daemon"))     # checks if thread is daemon thread.

answer = input("Do you wish to exit?\n")