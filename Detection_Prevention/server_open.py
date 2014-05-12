import Tkinter
import random
import os
#from ctcp import *
import tkMessageBox
from Tkinter import *
import sys  #for exit
from syn import *
blue ="#000fff000"
root = Tkinter.Tk()





def say():
  os.system("servertcp.py")



w = Tkinter.Canvas(root, width=400, height=300, background="#000000")
w.create_text(200,150,text="DOS ATTACK",font="Arial 20",fill="#ff0000")

w.pack()
 
flake = [];
moves = []
B = Tkinter.Button(root, text ="Continue with Client",command = say)
B.pack()

for i in range(50):
 flake.append(w.create_text(random.randrange(400),random.randrange(300),text="|",fill="#ffffff",font="Times 30"))
 moves.append([0.04 + random.random()/10,0.7 + random.random()])
try:
 while 1:
  for i in range(len(flake)):
   p = w.coords(flake[i])
   p[0]+=moves[i][0]
   p[1]+=moves[i][1]
   w.coords(flake[i],p[0],p[1])
   if(p[1]>310):
    w.coords(flake[i],random.randrange(400),-10)
   root.update_idletasks()
   root.update()
except Tkinter.TclError:
 pass



root.mainloop()

