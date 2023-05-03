import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import customtkinter as ctk
from tkinter.filedialog import askdirectory
from Services.app_services import *

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

threads = Threads()

services = Services()

class MyTabView(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        UIFont = ctk.CTkFont(family="Segoe UI", weight="bold")
        self.add("Download")
        self.add("Playlist")

        # Download Tab
        self.frame = ctk.CTkFrame(master=self.tab("Download"))
        self.frame.pack(pady=30, padx=60, fill="both", expand=True)
        label = ctk.CTkLabel(master=self.frame, text="Insert an YouTube link")
        label.pack(pady=12, padx=10)

        entry0 = ctk.CTkEntry(master=self.frame,
                              placeholder_text="Enter a valid link")
        entry0.pack(pady=10, padx=10)

        checkboxValue = ctk.IntVar()
        checkbox = ctk.CTkCheckBox(master=self.frame,
                                   text="Audio Only",
                                   variable=checkboxValue,
                                   onvalue=1,
                                   offvalue=0)
        checkbox.pack(pady=12, padx=10)

        downloadButton = ctk.CTkButton(
            hover_color="#035bbd",
            font=UIFont,
            master=self.frame,
            text="Download",
            command=lambda: threads.AudioThread(entry0.get())
            if checkboxValue.get() == 1 else threads.VideoThread(entry0.get()))
        downloadButton.pack(pady=12, padx=10)

        # Playlist Tab
        self.frame2 = ctk.CTkFrame(master=self.tab("Playlist"))
        self.frame2.pack(pady=30, padx=60, fill="both", expand=True)
        self.label = ctk.CTkLabel(master=self.frame2, text="Playlist")
        self.label.pack(pady=12, padx=10)

class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Pyload")
        # self.iconbitmap("../assets/icon.ico") // iconbitmap deprecado
        self.geometry("500x350")
     
        self.tab_view = MyTabView(master=self)
        self.tab_view.pack(padx=20, pady=20, fill="both", expand=True)

app = App()
app.mainloop()