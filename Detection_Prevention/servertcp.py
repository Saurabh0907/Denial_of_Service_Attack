import socket
import sys
from thread import *
try:
   s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error,msg:
   print "Socket Creation Error"
   sys.exit();

print 'Socket Created'
host = ''
port = 9022

try:
   s.bind((host, port))
except socket.error,msg:
   print "Bind Failed";
   sys.exit()

print "Socket bind complete"
s.listen(10)
print "Socket now listening"
CONNECTION_LIST = []

def clientthread(conn):
   i=0
   p=0
   while True:
      file = open("server.txt","a")
      p+=1
      data = conn.recv(1024)
      file.write("Client :");
      file.write(str(data));
      file.write("\n");
      reply = 'OK...' + data
      file.write("Server :");
      file.write(str(reply));
      file.write("\n");
      conn.send(reply)
      print data
      file.close()
      if p>200:
	conn.close()
	CONNECTION_LIST.remove(conn)

while True:
   conn, addr = s.accept()
   CONNECTION_LIST.append(conn)
   start_new_thread(clientthread,(conn,))

conn.close()
s.close()
      
