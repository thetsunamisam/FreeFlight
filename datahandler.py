from tkinter import *
unitMode = 'us' """metric,us,aviation"""
if unitMode == 'us':
    altunit = 'ft'
    speedunit = 'mph'
data = Tk()
speedunit = 'mph'
altunit = 'ft'
altitudeLabel = Label(data, text=('Alitude ' + altunit))
altitudeData = Label(data, text='No connection')
speedLabel = Label(data, text=('Speed ' + speedunit))
speedData = Label(data, text='No connection') 
latLabel = Label(data, text='Latitude')
latData = Label(data, text='No connection') 
lonLabel = Label(data, text='Longitude')
lonData = Label(data, text='No connection') 
pitchLabel = Label(data, text='Pitch')
pitchData = Label(data, text='No connection') 
rollLabel = Label(data, text='Roll')
rollData = Label(data, text='No connection') 
yawLabel = Label(data, text='Yaw')
yawData = Label(data, text='No connection') 
###grids
altitudeLabel.grid(row=0, column=0)
altitudeData.grid(row=0, column=1)
speedLabel.grid(row=1, column=0)
speedData.grid(row=1, column=1)
latLabel.grid(row=2, column=0)
latData.grid(row=2, column=1)
lonLabel.grid(row=3, column=0) 
lonData.grid(row=3, column=1)
pitchLabel.grid(row=4, column=0) 
pitchData.grid(row=4, column=1) 
yawLabel.grid(row=5, column=0)
yawData.grid(row=5, column=1) 

data.mainloop()
