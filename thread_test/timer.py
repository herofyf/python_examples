import threading

def hello():
    print('hello world')

def main():
    t = threading.Timer(5.0, hello)
    t.start()

if __name__ == '__main__':
    main()