import tkinter
import psutil


print('The cpu usage is: ', psutil.cpu_percent(4))
print('RAM memory % used is:' , psutil.virtual_memory()[2])
print('CPU freq:', psutil.cpu_freq()[0])
print('Disk usage:', psutil.disk_usage('/')[3])
print('swap memory:', psutil.swap_memory())

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

net = Button(root, text='Network')
net.pack()

cpu = Button(root, text='CPU')
cpu.pack()

disk = Button(root, text='Disk')
disk.pack()

mem = Button(root, text='Mamory')
mem.pack()


root.mainloop()
