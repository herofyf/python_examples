import threading

global_var = 0


def job1(sync):
    for i in range(3):
        sync.acquire()
        sync.acquire()
        global global_var
        global_var += 1
        threading._sleep(2)
        sync.release()
        sync.release()


def job2(sync):
    for i in range(3):
        sync.acquire()
        sync.acquire()
        global global_var
        global_var -= 1

        threading._sleep(1)
        sync.release()
        sync.release()

if __name__ == '__main__':
    sync = threading.RLock()
    t1 = threading.Thread(target=job1, args=(sync,))
    t2 = threading.Thread(target=job2, args=(sync,))
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(global_var)