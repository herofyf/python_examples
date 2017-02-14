import threading
import random

lock = threading.Lock()
# no value comes
not_empty_cond = threading.Condition(lock)

# list is full, writer should wait
full_cond = threading.Condition(lock)

# max items in list
full_num = 10

# to stop all of threads
quit = False

# values list
changed_val =  []

# console print lock
console_lock = threading.Lock()

def reader():

    while(quit == False):
        coming_values =[]
        not_empty_cond.acquire()

        '''
        to judge what condition can read, what condition job should be waiting

        '''
        global  changed_val
        while (len(changed_val) == 0):
            # to wait not empty
            not_empty_cond.wait()
            if (quit == True):
                break

        # check signal
        if (len(changed_val) != 0):
            coming_values = [x for x in changed_val]
            changed_val = []
            # let writer to write
            full_cond.notify()

        not_empty_cond.release()

        console_lock.acquire()
        print("read data:", coming_values)
        console_lock.release()
        threading._sleep(1)

def writer():
    while(quit == False):
        full_cond.acquire()

        global  changed_val
        '''
        to judge what condition can write, what condition job should be waiting
        '''
        while (len(changed_val) >= full_num):
            full_cond.wait()


        if (quit == False):
            x = random.randint(1, 2)
            changed_val.append(x)

            not_empty_cond.notify(1)

        full_cond.release()

        console_lock.acquire()
        print("write data:", x)
        console_lock.release()
        threading._sleep(1)

'''
    the whole test is check the same while read and write
'''
if __name__ == '__main__':
    threads = []
    for i in range(2):
        t = threading.Thread(target = reader)
        t.start()
        threads.append(t)


    t = threading.Thread(target= writer)
    t.start()
    threads.append(t)

    threading._sleep(10)

    # trigger stop all of threads
    quit = True
    full_cond.acquire()
    full_cond.notify_all()
    full_cond.release()

    not_empty_cond.acquire()
    not_empty_cond.notify_all()
    not_empty_cond.release()
    for t in threads:
        t.join()