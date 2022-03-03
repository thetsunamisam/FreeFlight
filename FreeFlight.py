from tkinter import *
from tkinter import messagebox
pfd = Tk()
messagebox.showwarning("Warning!", "Pls dont use this")
horizon = Button(pfd, text='Artificial Horizon')
datafeed = Button(pfd, text='Data Feed')
videofeeddigital = Button(pfd, text='Video (Digital)')
videofeedanalog = Button(pfd, text= 'Video (Analog)')
###packs
horizon.pack()
datafeed.pack()
videofeeddigital.pack()
videofeedanalog.pack()
pfd.mainloop()
