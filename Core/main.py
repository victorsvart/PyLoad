import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import customtkinter as ctk
from Services.app_services import *
from threading import Thread as th

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

threads = Threads()

services = Services()


class MyTabView(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        UIFont = ctk.CTkFont(family="Segoe UI", weight="bold")
        self.add("Download")

       

        # Download Tab
        self.frame = ctk.CTkFrame(master=self.tab("Download"))
        self.frame.pack(pady=30, padx=60, fill="both", expand=True)
        self.label = ctk.CTkLabel(master=self.frame, text="Insert an YouTube link")
        self.label.pack(pady=12, padx=10)

        self.entry0 = ctk.CTkEntry(master=self.frame,
                              placeholder_text="Enter a valid link")
        self.entry0.pack(pady=10, padx=10)

        self.checkboxValue = ctk.IntVar()
        self.checkbox = ctk.CTkCheckBox(master=self.frame,
                                   text="Audio Only",
                                   variable=self.checkboxValue,
                                   onvalue=1,
                                   offvalue=0)
        self.checkbox.pack(pady=12, padx=10)

       

        self.downloadButton = ctk.CTkButton(
            hover_color="#035bbd",
            font=UIFont,
            master=self.frame,
            text="Download",
            command=lambda: [self.progressBar.start(), self.handleThread()])
        self.downloadButton.pack(pady=12, padx=10)

        self.progressBar = ctk.CTkProgressBar(master=self.frame, orientation="horizontal", progress_color="darkgrey",  mode="undeterminate")
        self.progressBar.pack(pady=12, padx=10)




    def handleDownloads(self):
        self.progressBar.configure(mode="undeterminate", progress_color="darkcyan")
        if(self.checkboxValue.get() == 1):
           result = threads.AudioThread(self.entry0.get())
           if(result == True):
               self.progressBar.configure(mode="determinate", progress_color="green")
               self.progressBar.set(100)
               self.progressBar.stop()
               
            
        else:
            result = threads.VideoThread(self.entry0.get())
            if(result == True):
                self.progressBar.configure(mode="determinate", progress_color="green")
                self.progressBar.set(100)
                self.progressBar.stop()

    def handleThread(self):
        buttonThread = th(target=self.handleDownloads)
        buttonThread.start()
            
              
        
            
class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Pyload")
        # self.iconbitmap("../assets/icon.ico") // iconbitmap deprecado
        self.geometry("650x400")
        self.tab_view = MyTabView(master=self)
        self.tab_view.pack(padx=20, pady=20, fill="both", expand=True)

app = App()
app.mainloop()