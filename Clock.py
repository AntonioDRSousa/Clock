from tkinter import Label
from time import strftime
from datetime import datetime
from pytz import timezone

tz = 'UTC'

def setTimeZone(s):
    global tz
    tz = s

class Clock:
    def __init__(self,tab):    
        self.label = Label(tab,background='black',foreground='green1',font=('Helvatical bold',40))
        self.lweek = Label(tab,background='black',foreground='green1',font=('Helvatical bold',40))
        self.ldate = Label(tab,background='black',foreground='green1',font=('Helvatical bold',40))
        self.label.pack(fill='both',expand=1)
        self.lweek.pack(fill='both',expand=1)
        self.ldate.pack(fill='both',expand=1)
        self.time()

        
    def time(self):
        time = datetime.now(timezone(tz))
        string = time.strftime('%H:%M:%S')
        self.label.config(text=string)
        s1 = time.strftime("%A")
        self.lweek.config(text=s1)
        s2 = time.strftime("%d/%m/%Y")
        self.ldate.config(text=s2)
        self.label.after(1000,self.time)
    