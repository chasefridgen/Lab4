# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time, random

host = sys.argv[1]
textport = sys.argv[2]
n = 10;

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)

i = 0

while i < n:
    i += 1
    data = random.randint(1, 100)
    
#    s.sendall(data.encode('utf-8'))
    s.sendto(str(data).encode('utf-8'), server_address)

s.shutdown(1)

