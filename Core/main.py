import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import customtkinter as ctk
from Services.app_services import Threads as Threads
from threading import Thread as th
from Repositories.tableandwidget_handler import TabAndWidgetHandler

class MyTabView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Pyload")
        self.geometry("650x400")
        self._set_appearance_mode("dark")
        

        self.checkboxValue = ctk.IntVar()
        self.handler = TabAndWidgetHandler(master=self)
        self.handler.setTabAndFrame(tabName="Download")
        self.handler.setLabel(text="Insert an YouTube link", posy=12, posx=10)
        self.handler.setEntry(placeholder_text="Enter a valid link")
        self.handler.setCheckBox(text="Audio Only", variable=self.checkboxValue)
        self.handler.setProgressBar(orientation="horizontal", progress_color="#035bbd",  mode="undeterminate")
        self.handler.setButton(hover_color="#035bbd", text="Download", command=lambda: [self.handler.progressBar.start(),
                                                                                        self.handleThread()])

        
    def handleDownloads(self):
        threads = Threads()
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
app.mainloop()