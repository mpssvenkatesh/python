'''
Client application obtaining Date and Time

'''
import socket as s
from codecs import decode

# Communication channel and link set up

HOST = 'localhost'

PORT = 5000

ADDRESS = (HOST, PORT)

BUFSIZE = 1024

server = s.socket(s.AF_INET, s.SOCK_STREAM)

server.connect(ADDRESS)

#Process
msg = decode(server.recv(BUFSIZE), 'ascii')
print(msg)

while True:
    message = input('>')
    if not message:
        break
    server.send(bytes(message, 'ascii'))
    reply = decode(server.recv(BUFSIZE), 'ascii')

    if not reply:
        print('Server disconnected')
        break
    print(reply)

server.close()




    
    



