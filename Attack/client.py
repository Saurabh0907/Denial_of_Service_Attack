from Tkinter import *
import socket#for sockets
import sys  #for exit
import tkMessageBox
blue ="#000fff000"
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()
 
host = 'localhost';
port = 40030;



root = Tk()
frame = Frame(root)
frame.pack()
root.geometry("500x500")
e=NONE

def sendmsg():
 global e
 e = Entry(frame ,width=50 )
 e.pack(side=RIGHT)
 e.focus_set()
 b = Button(frame, text="send", width=10, command=callback ,bg =blue)
 b.pack(side=LEFT)
 mainloop()
 


def callback():
    while(1):
      
      print e.get()
      msg=str(e.get())
      e.delete(0, END)
    
      
     
      try :
        #Set the whole string
        text_area.insert(END,'Client:'+msg+'\n')
        s.sendto(msg, (host, port))
        
        # receive data from client (data, addr)
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

frame=Frame(root)
frame.pack()
text_area = Text(frame)
text_area.pack(side=BOTTOM)

B1 = Button(root, text = "CLOSE", command = sys.exit)
B1.pack(side =TOP)

root.mainloop()

