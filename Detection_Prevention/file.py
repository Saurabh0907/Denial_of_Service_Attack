from Tkinter import *
import tkMessageBox

root = Tk()
frame = Frame(root)
frame.pack()
root.geometry("500x500")
text_area = Text(frame)
text_area.pack(side=BOTTOM)

while(1):
 text_area.delete(1.0, END)   
 fo = open("server.txt", "r")
 str = fo.read(500000);
 text_area.insert(END,str+'\n')
 print "Read String is : ", str
 # Close opend file
 fo.close()
 


root.mainloop()
