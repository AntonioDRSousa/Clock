from tkinter import Tk, ttk
from Clock import *
from Stopwatch import *
from Settings import *

class Main:
    def __init__(self):
        win = Tk()
        win.geometry("300x300")
        win.title('Time')
        tabcontrol = ttk.Notebook(win)
        tab_clock = ttk.Frame(tabcontrol)
        tab_conf = ttk.Frame(tabcontrol)
        tab_timer = ttk.Frame(tabcontrol)
        tab_stopwatch = ttk.Frame(tabcontrol)
        tabcontrol.add(tab_clock,text='Clock')
        tabcontrol.add(tab_conf,text='Settings')
        tabcontrol.add(tab_timer,text='Timer')
        tabcontrol.add(tab_stopwatch,text='Stopwatch')
        tabcontrol.pack(expand=1,fill="both")
        
        Clock(tab_clock)
        Stopwatch(tab_stopwatch)
        Settings(tab_conf)
        
        win.mainloop()
        
if __name__=="__main__":
    Main()