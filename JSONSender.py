# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time, json

host = sys.argv[1]
textport = sys.argv[2]
n = 10

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)
i = 0

while i < 10:
    i += 1
    data = {"name": "john", "age": 30 + i, "city": "new York"}
    datay = json.dumps(data);
    
#    s.sendall(data.encode('utf-8'))
    s.sendto(datay.encode('utf-8'), server_address)

s.shutdown(1)

