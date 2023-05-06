from customtkinter import CTkTabview, CTkLabel, CTkEntry, CTkCheckBox, CTkButton, CTkProgressBar, CTkFrame, CTkFont
from abc import ABC, abstractmethod
from threading import Thread as th
from Services.app_services import Threads 
threads = Threads()
class TabAndWidgetHandler(CTkTabview):
    def __init__(self, master, **kwargs):
        self.checkboxValue = 1
        super().__init__(master, **kwargs)
    

    @abstractmethod
    def tabConfig(self, *args, **kwargs):
        self.configure(*args, **kwargs)
        
    @abstractmethod
    def addTab(self, quantity, tabName):
        self.tabNameList = []
        for tab in range(quantity):
            self.add(f"{tabName[tab]}")
            self.tabNameList.append(tabName[tab])
        return self.tabNameList

    @abstractmethod
    def setFrame(self, tabList, frameQuantity, tabName):
        frameList = []
        for frame in range(frameQuantity):
            self.frame = CTkFrame(master=self.tab(tabList[frame]))
            self.frame.pack(pady=30, padx=60, fill="both", expand=True)
            frameList.append(self.frame)
        return frameList
            

    @abstractmethod
    def setLabel(self, frame, text):
        self.label = CTkLabel(master=frame, text=text)
        self.label.pack(pady=12, padx=10)

    @abstractmethod
    def setEntry(self, frame, placeholder_text):
        self.entry = CTkEntry(master=frame, placeholder_text=placeholder_text)
        self.entry.pack(pady=12, padx=10)
    @abstractmethod
    def setCheckBox(self, frame, text, variable, onvalue=1, offvalue=0):
        self.checkbox = CTkCheckBox(master=frame, text=text, variable=variable, onvalue=onvalue, offvalue=offvalue)
        self.checkbox.pack(pady=12, padx=10)

    @abstractmethod
    def button(self, frame, hover_color, font, text, *args, **kwargs):
        self.button = CTkButton(master=frame, hover_color=hover_color, font=font, text=text, *args, **kwargs)
        self.button.pack(pady=12, padx=10)

    @abstractmethod
    def setProgressBar(self, frame, orientation, progress_color, mode):
        self.progressBar = CTkProgressBar(master=frame, orientation=orientation, progress_color=progress_color, mode=mode)
        return self.progressBar
    
    