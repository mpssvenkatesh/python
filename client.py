#Client side

import socket as s
from codecs import decode

HOST = 'localhost'

PORT = 5000
ADDRESS = (HOST, PORT)

BUFSIZE = 1024

server = s.socket(s.AF_INET, s.SOCK_STREAM)
server.connect(ADDRESS)

dayTime = decode(server.recv(BUFSIZE), 'ascii')
print(dayTime)

server.close
