import tkinter
import psutil

from tkinter import *
from tkinter import messagebox

root = Tk()

root.geometry(newGeometry=str('300x300'))
root.title('Monitor')
text = Label(root, text='System Monitor')
text.pack()



def cpu():
    messagebox.showinfo('The CPU usage is:', psutil.cpu_percent(4))


def fre():
    print('CPU freq:', psutil.cpu_freq()[0])
    messagebox.showinfo('CPU freq:', psutil.cpu_freq()[0])

def ram():
    print('RAM memory % used is:', psutil.virtual_memory()[2])
    messagebox.showinfo('RAM memory % used is:', psutil.virtual_memory()[2])

def disk():
    print('Disk usage:', psutil.disk_usage('/')[3])
    messagebox.showinfo('Disk usage:', psutil.disk_usage('/')[3])

def swap():
    print('Swap memory:', psutil.swap_memory()[3])
    messagebox.showinfo('Swap memory:', psutil.swap_memory()[3])

def sens():
    print('Sensors Temperature', psutil.sensors_temperatures()['acpitz'][0])
    messagebox.showinfo('Sensors Temperature', psutil.sensors_temperatures()['acpitz'][0])

def battery():
    print('Battery:', psutil.sensors_battery()[0])
    messagebox.showinfo('Battery:', psutil.sensors_battery()[0])


cpu = Button(root, text='CPU', command=cpu)
cpu.pack()

fre = Button(root, text='CPU Frequency', command=fre)
fre.pack()

ram = Button(root, text='Ram Memory', command=ram)
ram.pack()

disk = Button(root, text='Disk usage', command=disk)
disk.pack()

temp = Button(root, text='Temperature', command=sens)
temp.pack()

battery = Button(root, text='Battery', command=battery)
battery.pack()

root.mainloop()
