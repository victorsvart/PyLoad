from customtkinter import CTkTabview, CTkLabel, CTkEntry, CTkCheckBox, CTkButton, CTkProgressBar, CTkFrame, CTkFont
from abc import ABC, abstractmethod
from threading import Thread as th
from Services.app_services import Threads 
threads = Threads()
class TabAndWidgetHandler(CTkTabview):
    def __init__(self, master, **kwargs):
        self.master = master
        self.UIFont = CTkFont(family="Segoe UI", weight="bold")
        super().__init__(master, **kwargs)
    

    @abstractmethod
    def setTabAndFrame(self, tabName):
        self.add(tabName)
        self.frame = CTkFrame(master=self.tab(tabName))
        self.frame.pack(padx=20, pady=20, fill="both", expand=True)
            

    @abstractmethod
    def setLabel(self, text):
        self.label = CTkLabel(master=self.frame, text=text)
        self.label.pack(pady=12, padx=10)

    @abstractmethod
    def setEntry(self, *args, **kwargs):
        self.entry = CTkEntry(master=self.frame, *args, **kwargs)
        self.entry.pack(pady=12, padx=10)

    @abstractmethod
    def setCheckBox(self,text, variable):
        self.checkbox = CTkCheckBox(master=self.frame, text=text, variable=variable, onvalue=1, offvalue=0)
        self.checkbox.pack(pady=12, padx=10)

    @abstractmethod
    def setButton(self, hover_color, text, *args, **kwargs):
        self.button = CTkButton(master=self.frame, hover_color=hover_color, font=self.UIFont, text=text, *args, **kwargs)
        self.button.pack(pady=12, padx=10)

    @abstractmethod
    def setProgressBar(self, orientation, progress_color, mode):
        self.progressBar = CTkProgressBar(master=self.frame, orientation=orientation, progress_color=progress_color, mode=mode)
        self.progressBar.pack(pady=12, padx=10)

    @abstractmethod
    def onDownloadBar(self):
        self.progressBar.configure(mode="undeterminate", progress_color="darkcyan")

    @abstractmethod
    def afterDownloadBar(self):
        self.progressBar.configure(mode="determinate", progress_color="green")
        self.progressBar.set(100)
        self.progressBar.stop()

    