# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 11:57:59 2020

@author: João Victor Sierra
"""

import tkinter as tk
import time
from winsound import *

class Application:
    timeStr = "25:00"
    running = False
    counter = 3
    
    def __init__(self, master=None):  
        self.optionsButtonsContainer = tk.Frame(master)
        self.optionsButtonsContainer.pack()
        
        self.cronometerContainer = tk.Frame(master)
        self.cronometerContainer["bg"] = "white"
        self.cronometerContainer["relief"] = "ridge"
        self.cronometerContainer["borderwidth"]  = 5
        self.cronometerContainer.pack(fill="y")
        
        self.buttonsContainer = tk.Frame(master)
        self.buttonsContainer.pack()

        self.btnPomodoro = tk.Button(self.optionsButtonsContainer)
        self.btnPomodoro["text"] = "Pomodoro" 
        self.btnPomodoro["bg"] = "lightblue"
        self.btnPomodoro["command"] = lambda: self.evtBtnPomodoro()
        self.btnPomodoro.pack(side=tk.LEFT)
        
        self.btnShortBreak = tk.Button(self.optionsButtonsContainer)
        self.btnShortBreak["text"] = "Short Break";
        self.btnShortBreak["bg"] = "lightblue"
        self.btnShortBreak["command"] = lambda: self.evtBtnShortBreak()
        self.btnShortBreak.pack(side=tk.LEFT)
        
        self.btnLongBreak = tk.Button(self.optionsButtonsContainer)
        self.btnLongBreak["text"] = "Long Break";
        self.btnLongBreak["bg"] = "lightblue"
        self.btnLongBreak["command"] = lambda: self.evtBtnLongBreak()
        self.btnLongBreak.pack(side=tk.LEFT)
        
        self.labelCronometer = tk.Label(self.cronometerContainer)
        self.labelCronometer["text"] = "25:00"
        self.labelCronometer["font"] = ("Arial", "75", "bold")
        self.labelCronometer["bg"] = "white"
        self.labelCronometer.pack()
        
        self.btnStart = tk.Button(self.buttonsContainer)
        self.btnStart["text"] = "Start"
        self.btnStart["command"] = lambda: self.evtBtnStart()
        self.btnStart["bg"] = "green"
        self.btnStart.pack(side=tk.LEFT)
        
        self.btnStop = tk.Button(self.buttonsContainer)
        self.btnStop["text"] = "Stop"
        self.btnStop["command"] = lambda: self.evtBtnStop()
        self.btnStop["bg"] = "red"
        self.btnStop.pack(side=tk.LEFT)
        
        self.btnReset = tk.Button(self.buttonsContainer)
        self.btnReset["text"] = "Reset"
        self.btnReset["command"] = lambda: self.changeCronometerLabelText(self.timeStr)
        self.btnReset["bg"] = "lightgray"
        self.btnReset.pack(side=tk.LEFT)
    
        self.changeCronometerLabelText("25:00")
    def get_sec(self, time_str):
        m, s = time_str.split(':')
        return int(m) * 60 + int(s)
    
    def changeCronometerLabelText(self, text): 
        self.labelCronometer["text"] = text   
        
    def count(self):
        if self.running and self.counter >= 0:
            self.changeCronometerLabelText(str(time.strftime("%M:%S", time.gmtime(self.counter))))
        
            self.labelCronometer.after(1000, self.count)
            
            self.counter -= 1
            
        if self.counter == 0:
            PlaySound(r'resources\Alarm Sound.wav', SND_FILENAME)
            self.running = False
        
    def countTime(self):    
        self.count()
        
    def evtBtnStart(self):
        if self.running == False:
            self.running = True
        
            self.counter = self.get_sec(self.timeStr)
            
            self.countTime()
        
    def evtBtnStop(self):
        self.running = False
        
    def evtBtnReset(self):
        self.running = False
        self.counter = self.get_sec(self.timeStr)
        print(self.running)
        
    def evtBtnPomodoro(self):
        self.timeStr = "25:00"
        self.changeCronometerLabelText(self.timeStr)
        
        if self.running:
            self.evtBtnStart()
        
    def evtBtnShortBreak(self):
        self.timeStr = "05:00"
        self.changeCronometerLabelText(self.timeStr)
        
        if self.running:
            self.evtBtnStart()
        
    def evtBtnLongBreak(self):
        self.timeStr = "10:00"
        self.changeCronometerLabelText(self.timeStr)
    
        if self.running:
            self.evtBtnStart()
    
root = tk.Tk()
root.geometry("300x185")
root.title("Pomodoro Timer")
root.resizable(0, 0)
root.iconbitmap(r'resources\icons8-tomato-48.png')
Application(root)
root.mainloop()
