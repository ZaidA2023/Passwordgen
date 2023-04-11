import random
from tkinter import *
import tkinter as tk
import pyperclip

win = Tk()
win.geometry("200x100")


def ranspec():
    special = ['!','"','@','#','$','%','^','&','*','(',')','-','_','+','=','\\\\','|','{','[','}',']',';',':','<','>',',','.','?','/','`','~']
    return special[random.randint(0,30)]

def rannum():
    return random.randint(0, 9)

def ranalph():
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    wah = alphabet[random.randint(0,51)]
    return wah

def make():
    password = " "
    count = 0
    count=count+1
    for i in range(S1.get()):
        x = random.randint(0,2)
        if x == 0:
            password = password + ranspec()
        elif x==1:
            password = password + str(rannum())
        elif x==2:
            password = password + ranalph()
    display.configure(text=password)
    display.pack(side=TOP,pady=5)
    return password
    
 
display =Label(win,text="")
button_dict={}
option= ["Generate", "Copy"]

b2 = Button(text = "Copy")
S1 = Scale(win, from_=8, to=20, orient=HORIZONTAL)
def save():
    xa = make()
    S1.configure()
    b2.configure(command=lambda : pyperclip.copy(xa))
    b2.pack(side=TOP,pady=5)
b1 = Button(text = "Generate",  command=save)
b1.pack(side=TOP,pady=5)
S1.pack(side=TOP,pady=5)

win.mainloop()