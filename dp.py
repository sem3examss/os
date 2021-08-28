import threading
import random
import math
import time

class Philosopher(threading.Thread):
    running=True
    def __init__(self,index,forkonleft,forkonright):
        threading.Thread.__init__(self)
        self.index=index
        self.forkonleft=forkonleft
        self.forkonright=forkonright

    def run(self):
        while self.running:
            time.sleep(3)
            print("philosopher %s is hungry "%self.index)
            self.dine()

    def dine(self):
        fork1,fork2=self.forkonleft,self.forkonright
        while self.running:
            fork1.acquire()
            isfree=fork2.acquire(False)
            if isfree:
                break
            fork1.release()
            print('philosopher %s swaps the forks '%self.index)
            fork1,fork2=fork2,fork1

        else:
            return
        self.dining()
        fork1.release()
        fork2.release()

    def dining(self):
        print("philosopher %s is eating "%self.index)
        time.sleep(3)
        print("philosopher %s completed eating "%self.index)
        print("philosopher %s is thinking "%self.index)


forks=[threading.Semaphore() for i in range(5)]
philosophers=[Philosopher(i,forks[i%5],forks[(i+1)%5]) for i in range(5)]
Philosopher.running=True
for p in philosophers:
    p.start()

time.sleep(10)
Philosopher.running=False
time.sleep(6)
print("done")