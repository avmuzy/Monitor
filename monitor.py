import tkinter
import psutil



print('RAM memory % used is:', psutil.virtual_memory()[2])
print('CPU freq:', psutil.cpu_freq()[0])
print('Disk usage:', psutil.disk_usage('/')[3])
print('Swap memory:', psutil.swap_memory()[3])

from tkinter import *
root = Tk()

root.geometry(newGeometry=str('300x400'))
root.title('Monitor')
text = Label(root, text='System Monitor')
text.pack()


def cpu():
    print('The cpu usage is: ', psutil.cpu_percent(4))


def disk():
    print('Disk usage:', psutil.disk_usage('/')[3])


def swapmem():
    print('Swap memory:', psutil.swap_memory()[3])


cpu = Button(root, text='CPU', command=cpu)
cpu.pack()

disk = Button(root, text='Disk', command=disk)
disk.pack()

swapmem = Button(root, text='Swap Memory', command=swapmem)
swapmem.pack()


root.mainloop()
