import threading

def thread_job():
    print("this is an added thread, number is %s" %(threading.currentThread()))
    for i in range(1, 10):
        threading._sleep(1)

def main():
    added_thread = threading.Thread(target= thread_job)
    added_thread.start()
    print(threading.activeCount())
    print(threading.enumerate())
    print(threading.currentThread())
    added_thread.join()

if __name__ == '__main__':
    main()