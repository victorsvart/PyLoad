import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import customtkinter as ctk
from Services.app_services import *
from threading import Thread as th
from Repositories.tableandwidget_handler import TabAndWidgetHandler
threads = Threads()

services = Services()


class MyTabView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Pyload")
        self.geometry("650x400")
        self._set_appearance_mode("dark")
        

        self.checkboxValue = ctk.IntVar()
        self.handler = TabAndWidgetHandler(master=self)
        self.handler.setTabAndFrame(tabName="Download")
        self.handler.setLabel(text="Insert an YouTube link")
        self.handler.setEntry(placeholder_text="Enter a valid link")
        self.handler.setCheckBox(text="Audio Only", variable=self.checkboxValue)
        self.handler.setProgressBar(orientation="horizontal", 
                                   progress_color="#035bbd", 
                                    mode="undeterminate")
        self.handler.setButton(hover_color="#035bbd", text="Download", command=lambda: [self.handler.progressBar.start(),
                                                                                       self.handleThread()])

        self.handler.setTabAndFrame(tabName="Playlist")
        self.handler.pack(padx=20, pady=20, fill="both", expand=True)
        
        self.handler.pack(padx=20, pady=20, fill="both", expand=True)


        
       
        # self.playlistTab = TabAndWidgetHandler(self, tabName="Playlist")
        # self.setTabAndFrame()
        # self.playlistTab.setLabel(text="Insert an YouTube link")


        # UIFont = ctk.CTkFont(family="Segoe UI", weight="bold")
        # self.tabs = self.addTab(2, ["Download", "Playlist"])

        # self.checkboxValue = ctk.IntVar()
        # self.frameList = self.setFrame(self.tabs, self.tabs)
        # self.setLabel(self.frameList[0], "Insert an YouTube link")
        # self.setEntry(self.frameList[0], "Enter a valid link")
        # self.setCheckBox(self.frameList[0], "Audio Only", self.checkboxValue)
        # self.progressBar = self.setProgressBar(self.frameList[0], "horizontal", "#035bbd", "undeterminate")
        # self.button(self.frameList[0], "#035bbd", UIFont, "Download", command=lambda: [self.progressBar.start(), 
        #                                                                                self.handleThread()])
        # self.progressBar.pack(pady=12, padx=10)
        
    def handleDownloads(self):
        self.handler.onDownloadBar()
        if(self.checkboxValue.get() == 1):
           result = threads.AudioThread(self.handler.entry.get())
           if(result == True):
                self.handler.afterDownloadBar()
            
        else:
            result = threads.VideoThread(self.handler.entry.get())
            if(result == True):
                self.handler.afterDownloadBar()
                

    def handleThread(self):
        buttonThread = th(target=self.handleDownloads)
        buttonThread.start()

app = MyTabView()
# app.setAppConfig()
# app.setTabView(MyTabView)
app.mainloop()