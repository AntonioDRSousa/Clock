from tkinter import Label, ttk
from time import time

class Stopwatch:
    def __init__(self,tab):
        self.label = Label(tab, font = ("arial", 30),bg="black",fg="#00FF00",text="00:00:00:000")
        
        self.bstart = ttk.Button(tab,text="START")
        self.bstop = ttk.Button(tab,text="STOP")
        self.breset = ttk.Button(tab,text="RESET")
        
        self.bstart.grid(row=0,column=0,rowspan=1,columnspan=1)
        self.bstop.grid(row=0,column=1,rowspan=1,columnspan=1)
        self.breset.grid(row=0,column=2,rowspan=1,columnspan=1)
        self.label.grid(row=1,column=0,rowspan=1,columnspan=3)
        
        
        self.bstart.bind("<Button 1>", self.start)
        self.bstop.bind("<Button 1>", self.stop)
        self.breset.bind("<Button 1>", self.reset)
        
        self.flag = True

    def start(self,event):
        self.id_time = None
        if self.flag:
            self.t0 = time()
        else:
            self.t0 += (time()-self.t1)
        self.flag = True
        self.timer()
        
    def stop(self,event):
        self.flag = False
        self.label.after_cancel(self.id_time)
        
    def reset(self,event):
        self.flag = True
        self.t0 = 0
        self.t1 = 0
        self.label.configure(text="00:00:00:000")
        self.label.after_cancel(self.id_time)
        
    def timer(self):
        self.t1 = time()
        dt = self.t1-self.t0
        
        milseconds = int((dt*1000)%1000)
        seconds = int(dt%60)
        minutes = int((dt % (3600))//60)
        hours = int(dt //(3600))
        
        self.label.configure(text=f"{hours:02}:{minutes:02}:{seconds:02}:{milseconds:03}")

        self.id_time=self.label.after(1, self.timer) 