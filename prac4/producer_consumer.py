import threading
import time

buffer = [0, 0, 0, 0, 0, 0, 0, 0]
empty = (len(buffer))
full = (0) 
mutex = 1 # binary semaphore
i =0
j= 0
def signal(param):
    param+=1
def wait(param):
    param-=1

def producer():
    global i
    while True:
        wait(empty)
        wait(mutex)
        print(f"item {i} is being produced")
        signal(mutex)
        signal(full)
        buffer[i] =1
        print(buffer,"\n")
        i= (i + 1) % len(buffer)
        time.sleep(1)  # Producer sleeps for 1 second

def consumer():
    global j
    while True:
        wait(full)
        wait(mutex)
        print(f"item {j} is being consumed")
        signal(mutex)
        signal(empty)
        buffer[j] = 0
        print(buffer,"\n")
        j=(j + 1) % len(buffer)
        time.sleep(2)  # Consumer sleeps for 2 seconds

t1=threading.Thread(target=producer)
t2=threading.Thread(target=consumer)
t1.start()
t2.start()

# Printing condition where access is blocked
while True:
    wait(mutex)
    if not full:
        print("Access is blocked: Buffer is empty")
    elif not empty:
        print("Access is blocked: Buffer is full")
    signal(mutex)
    time.sleep(2)  # Check every 2 seconds