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
    def __init__(self, Name, C):
        super(Send, self).__init__()
        self.name = Name
        self.c = C

    def run(self):
        while True:
            user_send = input("")
            # FOR ENDING THE DATA
            if user_send == "exit":
                self.c.close()
                exit()
            box = [self.name, ":", user_send]
            box1 = ''.join(box)

            # SENDING DATA TO SENDER
            self.c.send(bytes(box1, 'utf-8'))

# __main()__
# FOR SETTING IP TYPE
c = socket.socket()
# FOR CONNECTING WITH SERVER
c.connect(('192.168.1.6', 9999))
# TAKING SENDER NAME
name = input("ENTER YOUR NAME: ")

while True:
    # TAKING USER DATA FOR SENDING
    thread1 = Recieve(c)
    thread2 = Send(name, c)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
