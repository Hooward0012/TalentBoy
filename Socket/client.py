# import socket
#
# HOST = '127.0.0.1'
# PORT = 8080
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     s.sendall(b'Hello')
#     data = s.recv(1024)
# print('Received', repr(data))

import socket

host = '127.0.0.1'
port = 8080

s = socket.socket()
s.connect((host, port))
msg = s.recv(1024)
print(msg)