import socket

from threading import Thread

host = '127.0.0.1'
port = 8080

client = {}
addresses = {}

accept_num = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))


def handle_client_in(conn, addr):
    nikename = conn.recv(1024).decode('utf8')
    welcome = f'欢迎{nikename}加入聊天室\n'
    client[conn] = nikename
    brodcast(bytes(welcome, 'utf8'))

    while True:
        try:
            msg = conn.recv(1024)
            brodcast(msg, nikename + ':')
        except:
            conn.close()
            del client[conn]
            brodcast(bytes(f'{nikename}离开聊天室\n', 'utf8'))


def brodcast(msg, nikename=''):
    for conn in client:
        conn.send(bytes(nikename, 'utf8') + msg)


if __name__ == '__main__':
    s.listen(accept_num)
    print('服务器已经开启，正在监听client request')

    while True:
        conn, address = s.accept()
        print(address, '建立连接')
        conn.send('欢迎你来到我的chartroom，please enter your name for charting\n'.encode('utf8'))
        addresses[conn] = addresses
        Thread(target=handle_client_in, args=(conn, address)).start()
