from multiprocessing import Process
import time

def worker():
    print("Child process starting")
    time.sleep(2)
    print("Child process done")

p = Process(target=worker)
p.start()
print("Main process continues")
p.join()
print("All done")
