import socket
from threading import Thread
import sys

class Recieve(Thread):
    def __init__(self, C):
        super(Recieve, self).__init__()
        self.c = C

    def run(self):
        while True:
            # FETCHING SENDER MESSAGE
            user_rev = self.c.recv(1024).decode()
            print("\n" + user_rev)
            if not user_rev:
                break

class Send(Thread):
    def __init__(self, Name, C, S):
        super(Send, self).__init__()
        self.name = Name
        self.c = C
        self.s = S

    def run(self):
        while True:
            user_send = input("")
            if user_send == "exit":
                self.s.close()
                exit()
            box = [self.name, ":", user_send]
            box1 = ''.join(box)
            # FOR ENDING THE DATA
            # SENDING DATA TO SENDER
            self.c.send(bytes(box1, 'utf-8'))

# FOR SETTING IP TYPE
s = socket.socket()
print('Socket Created')

# FOR SETTING IP AND PORT NO
s.bind(('192.168.1.6', 9999))

# FOR SETTING NO OF DEVICE CAN LISTEN
s.listen(3)
print('Wait for connection')

# TAKING NAME
name = input("ENTER YOUR NAME: ")

while True:
    # FETCHING USER IP AND PORT NO
    c, addr = s.accept()
    print("Connected with", addr)
    
    thread1 = Recieve(c)
    thread2 = Send(name, c, s)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
