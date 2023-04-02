import random
import tkinter as tk
from tkinter import *
import pyperclip

win = Tk()
win.geometry("200x100")


def ranspec():
    special = ['!','"','@','#','$','%','^','&','*','(',')','-','_','+','=','\\\\','|','{','[','}',']',';',':','<','>',',','.','?','/','`','~']
    return special[random.randint(0,30)]

def rannum():
    return random.randint(0, 9)

def ranalph():
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    wah = alphabet[random.randint(0,25)]
    return wah

def make():
    password = " "
    count = 0
    count=count+1
    for i in range(20):
        x = random.randint(0,2)
        if x == 0:
            password = password + ranspec()
        elif x==1:
            password = password + str(rannum())
        elif x==2:
            password = password + ranalph()
    display.configure(text=password)
    display.pack()
    return password
    
 
display =Label(win,text="")
button_dict={}
option= ["Generate", "Copy"]

b2 = Button(text = "Copy")
def save():
    xa = make()
    b2.configure(command=lambda : pyperclip.copy(xa))
    b2.pack()
b1 = Button(text = "Generate",  command=save)
b1.pack()
win.mainloop()





