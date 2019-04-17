from tkinter import *
import subprocess

def callback():
    print ("clicked")
    #Voice.main()
    subprocess.call("Voice.py",shell=True)

my_window = Tk()
my_window.geometry("500x500")
theLabel = Label(my_window, text="test test test")
theLabel.pack(pady=10)
b = Button(my_window, text="click me", command=callback)
b.pack(pady=10)
my_window.mainloop()
print(id(my_window), type(my_window))
