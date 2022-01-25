import socket
from threading import *

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 9998))
print("Client is connected...")
is_stop_thread = False


# ---------------- Sub-class of Thread used for multi-threading ---------#
class ClientThrading(Thread):
    def __init__(self,
                 conn):
        Thread.__init__(self)
        self.connection = conn

    def send_msg(self, msg):
        self.connection.send(bytes(msg, 'utf-8'))

    def rec_msg(self):
        received = self.connection.recv(1024).decode()
        return received

    def getauthenticate(self):
        return self.is_authenticate

    def run(self):
        nameOfThread = current_thread().getName()
        while True:
            # global is_stop_thread
            # if is_stop_thread:
            #     break
            if nameOfThread == 'Send':
                # print("----In send thread-----")
                message = input()
                if message == 'exit':
                    # is_stop_thread = True
                    client.close()
                    break
                else:
                    self.connection.send(bytes(message, 'utf-8'))
                # print("-----Exit send thread-----")
            elif nameOfThread == 'Receive':
                # print("----In Receive thread--------")
                receivedMessage = self.connection.recv(1024).decode()
                print(receivedMessage)


receive = ClientThrading(client)
receive.setName('Receive')

send = ClientThrading(client)
send.setName('Send')
receive.start()
send.start()

receive.join()
send.join()
