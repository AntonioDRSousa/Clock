import tkinter as tk
from tkinter import ttk, Label
from pytz import all_timezones
from Clock import setTimeZone

class Settings:
    def __init__(self,tab):
        label = Label(tab,text="Time Zones")
        
        self.selected = tk.StringVar()
        time_zones = ttk.Combobox(tab, textvariable=self.selected)
        time_zones['values']=all_timezones
        time_zones['state'] = 'readonly'
        
        label.pack()
        time_zones.pack()
        
        time_zones.bind('<<ComboboxSelected>>', self.change_time_zone)
        
    def change_time_zone(self,event):
        setTimeZone(self.selected.get())
        
    