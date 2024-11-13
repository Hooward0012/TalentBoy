import socket
from tkinter import *
from threading import *

def get_msg():
    while True:
        try:
            msg = s.recv(1024).decode('utf8')
            text_message.insert(END, msg)
        except:
            break


def send():
    print('触发了发送按钮事件。。。')
    send_msg = text_text.get('0.0', END)
    s.send(bytes(send_msg, 'utf8'))
    text_text.delete('0.0', END)



root = Tk()
root.title('聊天室')

root.bind('<Return>', send)












message_frame = Frame(width=480, height=300, bg='white')
text_frame = Frame(width=480, height=100)
send_frame = Frame(width=480, height=30)

text_message = Text(message_frame)
text_text = Text(text_frame)
button_send = Button(send_frame, text='发送', command=send)

message_frame.grid(row=0, column=0, padx=3, pady=6)
text_frame.grid(row=1, column=0, padx=3, pady=6)
send_frame.grid(row=2, column=0)

message_frame.grid_propagate(0)
text_frame.grid_propagate(0)
send_frame.grid_propagate(0)

text_message.grid()
text_text.grid()
button_send.grid()


# socket 接入
host = '127.0.0.1'
port = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
receive_thread = Thread(target=get_msg)
receive_thread.start()

root.mainloop()