# multiprocessing   = running tasks in parallel on different CPU cores, bypasses GIL used for multithreading.

# multiprocessing   --> better for CPU bound tasks (heavy CPU usage)
# multithreading    --> better for io bounds tasks (waiting around for input)

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():
    print(cpu_count())
    
    start_time = time.perf_counter()

    a = Process(target=counter, args=(5*1000000,))
    a.start()

    b = Process(target=counter, args=(5*1000000,))
    b.start()

    c = Process(target=counter, args=(5*1000000,))
    c.start()

    d = Process(target=counter, args=(5*1000000,))
    d.start()

    a.join()
    b.join()
    c.join()
    d.join()

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print("finished in",round(elapsed_time,4),"seconds")

if __name__ == "__main__":      # this is needed to ensure that no child processes are created before the start of main function
    main()