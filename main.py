# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 11:57:59 2020

@author: João Victor Sierra
@description: an Pomodoro Timer written in Python
"""

import tkinter as tk
import time
from winsound import *
import configparser

def readConfigFile():
    config = configparser.ConfigParser()
    
    config.read("config.ini")
    
    values = (config["DEFAULT"]["PomodoroTime"], config["DEFAULT"]["ShortBreakTime"],
              config["DEFAULT"]["LongBreakTime"]) 
    
    return values

class MainWindow:
    timeStr = ""
    
    pomodoroValue = ""
    shortBreakValue = ""
    longBreakValue = ""
    
    running = False
    counter = 3
    
    def setTimeOptions(self):
        self.pomodoroValue, self.shortBreakValue, self.longBreakValue = readConfigFile()
    
        self.pomodoroValue += ":00"
        self.shortBreakValue += ":00"
        self.longBreakValue += ":00"

        self.pomodoroValue = str(time.strftime("%M:%S", time.strptime(self.pomodoroValue, "%M:%S")))
        self.shortBreakValue = str(time.strftime("%M:%S", time.strptime(self.shortBreakValue, "%M:%S")))
        self.longBreakValue = str(time.strftime("%M:%S", time.strptime(self.longBreakValue, "%M:%S")))

        self.changeCronometerLabelText(self.pomodoroValue)
    
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
        
        self.footerContainer = tk.Frame(master)
        self.footerContainer.pack()

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
    
        self.btnOptions = tk.Button(self.footerContainer)
        self.btnOptions["text"] = "Options"
        self.btnOptions["command"] = lambda: self.evtBtnOptions()
        self.btnOptions.pack()
    
        self.setTimeOptions()
    def get_sec(self, time_str):
        m, s = time_str.split(':')
        return int(m) * 60 + int(s)
    
    def changeCronometerLabelText(self, text): 
        self.timeStr = text
        self.labelCronometer["text"] = text   
        
    def count(self):
        if self.running and self.counter >= 0:
            self.changeCronometerLabelText(str(time.strftime("%M:%S", time.gmtime(self.counter))))
        
            self.labelCronometer.after(1000, self.count)
            
            self.counter -= 1
            
        if self.counter == 0:
            PlaySound('Alarm Sound.wav', SND_FILENAME)
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
        self.changeCronometerLabelText(self.pomodoroValue)
        
    def evtBtnShortBreak(self):
        self.changeCronometerLabelText(self.shortBreakValue)
        
    def evtBtnLongBreak(self):
        self.changeCronometerLabelText(self.longBreakValue)

    def evtBtnOptions(self):
        rootOpt = tk.Toplevel()
        ConfigurationWindow(rootOpt)
        rootOpt.title("Options")
        rootOpt.resizable(0, 0)
        rootOpt.iconbitmap(r'C:\Users\Pichau\.spyder-py3\Pomodoro\resources\icons8-tomato-48.png')
        rootOpt.geometry("250x150")
        rootOpt.mainloop()

class ConfigurationWindow:
    def __init__(self, master=None):  
            self.entriesContainer = tk.Frame(master)
            self.entriesContainer.pack()
            
            self.lblPomodoro = tk.Label(self.entriesContainer)
            self.lblPomodoro["text"] = "Pomodoro Time"
            self.lblPomodoro.pack()
            
            self.entryPomodoro = tk.Entry(self.entriesContainer)
            self.entryPomodoro.pack()
            
            self.lblShortBreak = tk.Label(self.entriesContainer)
            self.lblShortBreak["text"] = "Short Break Time"
            self.lblShortBreak.pack()
            
            self.entryShortBreak = tk.Entry(self.entriesContainer)
            self.entryShortBreak.pack()
            
            self.lblLongBreak = tk.Label(self.entriesContainer)
            self.lblLongBreak["text"] = "Long Break Time"
            self.lblLongBreak.pack()
            
            self.entryLongBreak = tk.Entry(self.entriesContainer)
            self.entryLongBreak.pack()
            
            self.btnSave = tk.Button(self.entriesContainer)
            self.btnSave["text"] = "Save Options"
            self.btnSave["bg"] = "lightblue"
            self.btnSave["command"] = lambda: self.saveConfiguration()
            self.btnSave.pack()
         
            self.setEntryValues()
            
    def setEntryValues(self):
        pomodoro, short, long = readConfigFile()        
            
        self.entryPomodoro.delete(0, tk.END)
        self.entryPomodoro.insert(0, pomodoro)
        
        self.entryShortBreak.delete(0, tk.END)
        self.entryShortBreak.insert(0, short)
        
        self.entryLongBreak.delete(0, tk.END)
        self.entryLongBreak.insert(0, long)
        
    def saveConfiguration(self):
        config = configparser.ConfigParser()
        
        config["DEFAULT"] = {"PomodoroTime": self.entryPomodoro.get(),
                             "ShortBreakTime": self.entryShortBreak.get(),
                             "LongBreakTime": self.entryLongBreak.get()}
        
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

root = tk.Tk()
root.title("Pomodoro Timer")
root.resizable(0, 0)
root.iconbitmap(r'C:\Users\Pichau\.spyder-py3\Pomodoro\resources\icons8-tomato-48.png')
MainWindow(root)
root.mainloop()
