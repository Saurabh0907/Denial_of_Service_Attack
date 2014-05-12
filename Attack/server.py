import socket
import sys
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 40034 # Arbitrary non-privileged port
 
# Datagram (udp) socket
try :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print 'Socket created'
except socket.error, msg :
    print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
 
 
# Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
#now keep talking with the client
while 1:
    # receive data from client (data, addr)
    file = open("server.txt","a")
    d = s.recvfrom(1024)

    file.write("Client :");
    file.write(str(d));
    file.write("\n");
    data = d[0]
    addr = d[1]
     
    if not data: 
        break
     
    reply = 'OK...' + data
    file.write("Server :");
    file.write(str(reply));
    file.write("\n");
    
    s.sendto(reply , addr)
    print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()
    file.close()
s.close()
