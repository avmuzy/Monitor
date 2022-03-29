import psutil
from tkinter import *
from tkinter import messagebox

root = Tk()

root.geometry(newGeometry=str('300x400'))
root.title('Monitor')
text = Label(root, text='System Monitor')
text.pack()


def cpu():

    print('The cpu usage is: ', psutil.cpu_percent(4))
    messagebox.showinfo('The cpu usage is: ', psutil.cpu_percent(4))

def disk():
    print('Disk usage:', psutil.disk_usage('/')[3])
    messagebox.showinfo('Disk usage:', psutil.disk_usage('/')[3])


def swapmem():
    print('Swap memory:', psutil.swap_memory()[3])
    messagebox.showinfo('Swap memory:', psutil.swap_memory()[3])


def ram():
    print('RAM memory % used is:', psutil.virtual_memory()[2])
    messagebox.showinfo('RAM memory % used is:', psutil.virtual_memory()[2])


cpu = Button(root, text='CPU', command=cpu)
cpu.pack()

disk = Button(root, text='Disk', command=disk)
disk.pack()

swapmem = Button(root, text='Swap Memory', command=swapmem)
swapmem.pack()

ram = Button(root, text='Ram Memory', command=ram)
ram.pack()


root.mainloop()
