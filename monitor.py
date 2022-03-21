import tkinter
from tkinter import *
root = Tk()

root.geometry(newGeometry=str('300x400'))
root.title('Monitor')
text = Label (root, text='System Monitor')
text.pack()

temp = Button(root, text='temperature')
temp.pack()

fan = Button(root, text='Fan speed')
fan.pack()







root.mainloop()
