# http://scotdoyle.com/python-epoll-howto.html

# because this script uses epoll which based on unix/linux. so can't run in windows os

import socket, select

EOL1 = b'\n\n'
EOL2 = b'\r\n'
response  = b'HTTP/1.0 200 OK\r\nDate: Mon, 1 Jan 1996 01:01:01 GMT\r\n'
response += b'Content-Type: text/plain\r\nContent-Length: 13\r\n\r\n'
response += b'Hello, world!'

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind(('0.0.0.0', 8080))
serversocket.listen(10)
serversocket.setblocking(0)

epoll = select.epoll()
epoll.register(serversocket.fileno(), select.EPOLLIN)

try:
    connections = {}; requests = {}; responses = {}

    while True:
        events = epoll.poll(10)
        for fileno, event in events:
            if fileno == serversocket.fileno():
                # get new client socket
                connection, address = serversocket.accept()
                connection.setblocking(0)
                epoll.register(connection.fileno(), select.EPOLLIN)
                connections[connection.fileno()] = connection
                requests[connection.fileno()] =  b''
                responses[connection.fileno()] = response
            elif event & select.EPOLLIN:
                requests[fileno] += connections[fileno].recv(1024)
                if EOL1 in requests[fileno] or EOL2 in requests[fileno]:
                    epoll.modify(fileno, select.EPOLLOUT | select.EPOLLIN)
                    print('-' * 40 + '\n' + requests[fileno].decode()[:-2])
            elif event & select.EPOLLOUT:
                byteswritten = connections[fileno].send(responses[fileno])
                responses[fileno] = responses[fileno][byteswritten:]
                if len(responses[fileno]) == 0:
                    try:
                        actions =  input('do you receive or close or send? r/c/s')
                        if actions == 'r':
                            epoll.modify(fileno, select.EPOLLIN)
                        elif actions == 'c':
                            epoll.modify(fileno, 0)
                            connections[fileno].shutdown(socket.SHUT_RDWR)
                        elif actions == 's':
                            epoll.modify(fileno, select.EPOLLOUT)
                    except:
                        pass

            elif event & select.EPOLLHUP:
                epoll.unregister(fileno)
                connections[fileno].close()
                del connections[fileno]


finally:
    epoll.unregister(serversocket.fileno())
    epoll.close()
    serversocket.close()