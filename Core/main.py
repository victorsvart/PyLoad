import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import customtkinter as ctk
from Services.app_services import *
from threading import Thread as th
from Repositories.app_handler import App
from Repositories.tableandwidget_handler import TabAndWidgetHandler
threads = Threads()

services = Services()


class MyTabView(TabAndWidgetHandler):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        UIFont = ctk.CTkFont(family="Segoe UI", weight="bold")
        self.tabs = self.addTab(2, ["Download", "Playlist"])

        self.checkboxValue = ctk.IntVar()
        self.frameList = self.setFrame(self.tabs, 2, self.tabs)
        self.setLabel(self.frameList[0], "Insert an YouTube link")
        self.setEntry(self.frameList[0], "Enter a valid link")
        self.setCheckBox(self.frameList[0], "Audio Only", self.checkboxValue)
        self.progressBar = self.setProgressBar(self.frameList[0], "horizontal", "#035bbd", "undeterminate")
        self.button(self.frameList[0], "#035bbd", UIFont, "Download", command=lambda: [self.progressBar.start(), 
                                                                                       self.handleThread()])
        self.progressBar.pack(pady=12, padx=10)


        # Download Tab
        # self.frame = ctk.CTkFrame(master=self.tab("Download"))
        # self.frame.pack(pady=30, padx=60, fill="both", expand=True)
        # self.label = ctk.CTkLabel(master=self.frame, text="Insert an YouTube link")
        # self.label.pack(pady=12, padx=10)

        # self.entry0 = ctk.CTkEntry(master=self.frame,
        #                       placeholder_text="Enter a valid link")
        # self.entry0.pack(pady=10, padx=10)

        # self.checkboxValue = ctk.IntVar()
        # self.checkbox = ctk.CTkCheckBox(master=self.frame,
        #                            text="Audio Only",
        #                            variable=self.checkboxValue,
        #                            onvalue=1,
        #                            offvalue=0)
        # self.checkbox.pack(pady=12, padx=10)

       

        # self.downloadButton = ctk.CTkButton(
        #     hover_color="#035bbd",
        #     font=UIFont,
        #     master=self.frame,
        #     text="Download",
        #     command=lambda: [self.progressBar.start(), self.handleThread()])
        # self.downloadButton.pack(pady=12, padx=10)

        # self.progressBar = ctk.CTkProgressBar(master=self.frame, orientation="horizontal", progress_color="darkgrey",  mode="undeterminate")
        # self.progressBar.pack(pady=12, padx=10)


        # # Playlist Tab
        # self.frame2 = ctk.CTkFrame(master=self.tab("Playlist"))
        # self.frame2.pack(pady=30, padx=60, fill="both", expand=True)
        # self.label = ctk.CTkLabel(master=self.frame2, text="Playlist")
        # self.label.pack(pady=12, padx=10)
    def printsomething(self):
        print("hello")

    def handleDownloads(self):
        self.progressBar.configure(mode="undeterminate", progress_color="darkcyan")
        if(self.checkboxValue.get() == 1):
           result = threads.AudioThread(self.entry.get())
           if(result == True):
               self.progressBar.configure(mode="determinate", progress_color="green")
               self.progressBar.set(100)
               self.progressBar.stop()
               
            
        else:
            result = threads.VideoThread(self.entry.get())
            
            if(result == True):
                self.progressBar.stop()

    def handleThread(self):
        buttonThread = th(target=self.handleDownloads)
        buttonThread.start()

app = App("Pyload", 650, 400, "dark")
app.setAppConfig()
app.setTabView(MyTabView)
app.mainloop()