#Server

import socket as s
import time

HOST = 'localhost'

PORT = 5000
ADDRESS = (HOST, PORT)

BUFSIZE = 1024

server = s.socket(s.AF_INET, s.SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)

while True:
    print('...Waiting for connection ')

    client, address = server.accept()
    client.send(bytes(time.ctime()+'/n Have a Nice Day', 'ascii'))
    client.close()
