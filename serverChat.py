'''
This server application provides date and time
'''
import socket as s
from time import ctime
from codecs import decode

HOST = 'localhost'

PORT = 5000

ADDRESS = (HOST, PORT)

BUFSIZE = 1024

server = s.socket(s.AF_INET, s.SOCK_STREAM)

server.bind(ADDRESS)

server.listen(5)

while True:
    print('Waiting for connection . . . ')

    client, address = server.accept()

    print(' . . . connected from', address)

    client.send(bytes('Welcome to my chat room !!', 'ascii'))  #  1st MESSAGE

    while True:

        message = decode(client.recv(BUFSIZE), 'ascii')

        if not message:
            print('Client disconnected')
            client.close()
            break
        else:
        
            print(message)
            client.send(bytes(input('> '), 'ascii'))

    







