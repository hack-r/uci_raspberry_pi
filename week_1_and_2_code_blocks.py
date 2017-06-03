# these are just notes, this is not a runnable .py

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname("www.google.com")
mysock.connect((host, 80))
message = "GET / HTTP/1.1\r\n\r\n"
mysock.sendall(message.encode())
data=mysock.recv(1000)
mysock.close()

~~~~~~~~~~~~~~~~~~~~~~~

try:
     z = x / y
except ZeroDivisionError:
     print("Divide by zero")

Sock Exceptions:
sock.error -- all socket errors
gaierror  -- getaddressinfo() error - no host found

~~~~~~~~~~~~~~~~~~~~~~~

import socket
import sys

try:
     mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
     print("Failed to create socket")
     sys.exit()
try:
     host = socket.gethostbyname("www.google.com")
except socket.gaierror:
     print("Failed to get host")
     sys.exit()
mysock.connect((host, 80))
message = "GET / HTTP/1.1\r\n\r\n"
try:
     mysock.sendall(message.encode())
except socket.error:
     print("Failed to send")
     sys.exit()
data=mysock.recv(1000)
print(data)
mysock.close()

~~~~~~~~~~~~~~~~~~~~~~~~~~

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.bind("",1234)

mysock.listen(5)
conn, addr = mysock.accept()

note: listen() starts listening for a connect(), it is a "backlog", number of requests allowed to wait for service
accept() accepts a connection request, returns IP and port
~~~~~~~~~~~~~~~~~~~~~~~~~~

data = conn.recv(1000)
conn.sendall(data)

conn.close()
mysock.close()

~~~~~~~~~~~~~~~~~~~~~~~~~~
import socket
import sys

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
     mysock.bind("",1234)
except socket.error:
     print("Failed to bind")
     sys.exit()
mysock.list(5)
while True:
     conn, addr = mysock.accept()
     data = conn.recv(1000)
     if not data:
         break
     if data == b'on':
         GPIO.ouput(13, True)
     if data == b'off':
         GPIO.output(13, False)

conn.close()
mysock.close()
~~~~~~~~~~~
nc -l 1234
~~~~~~~~~~~~~~
import socket
ms = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ainfo = socket.getaddrinfo("127.0.0.1",1234)
print(ainfo)
print(ainfo[0][4])
ms.connect(ainfo[0][4])
ms.sendall(b"Hello World")
ms.close()
~~~~~~~~~~~~~~~~~
nc 127.0.0.1 1234 # don't do this until after ms.accept()

hello world
~~~~~~~~~~~~~~~~~
import socket
ms = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ainfo = socket.getaddrinfo(None,1234)
ms.bind(ainfo[0][4])
ms.listen(5)
conn,addr=ms.accept()
data = conn.recv(1000)
print(data)
conn.close()
