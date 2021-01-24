import socket
import time
import sys

class server():
    host = 'local host'
    port = 5000
    timeout = 15
    s = socket.socket(socket.AF_INET,
                      socket.SOCK_STREAM)
    s.bind(('', port))
    s.settimeout(timeout)
    s.listen(1)
    c, addr = s.accept()
    print("CONNECTION FROM:", str(addr))

    def send(self, msg):
        self.c.send(bytes(msg, "utf-8"))

    def close(self, msg="Closing connection"):
        self.c.send(msg.encode())
        self.c.close()
