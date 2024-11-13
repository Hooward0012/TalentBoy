# import socket
#
# HOST = '127.0.0.1'
# PORT = 8080
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen(1)
#     conn, addr = s.accept()
#     with conn:
#         print('Connected by', addr)
#         while True:
#             data = conn.recv(1024)
#             if not data: break
#             conn.sendall(data)

import socket

host = '127.0.0.1'
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen()
conn, addr = s.accept()
print(f'接受来自{addr}的连接，现在通信启动')
conn.send(b'fuck')