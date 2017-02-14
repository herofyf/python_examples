import threading
import time
from Queue import Queue


# pass list
def job(l, q):
    sum = 0;
    for i in range(len(l)):
        l[i] = l[i] **2
        sum += l[i]
    q.put(sum)

def main():
    q = Queue()
    threads = []
    data = [[1, 2], [4, 5], [1,1], [2,2]]
    for i in range(4):
        t = threading.Thread(target=job, args=(data[i], q))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    # to return result
    for i in range(4):
        print(q.get())

if __name__ == '__main__':
    main()
