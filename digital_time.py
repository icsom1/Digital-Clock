from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title('Digital Clock')

def time():
    String = strftime('%m-%d-%y:%H:%M:%S %p')
    label.config(text=String)
    label.after(1000, time)

label = Label(root, font=('Arial', 70), background='purple', foreground='white')
label.pack(anchor='center')


time()
mainloop()