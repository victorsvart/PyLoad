import customtkinter as ctk
from abc import ABC, abstractmethod

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def setAppConfig(self, title, width, height):
        self.title(title)
        self.geometry(f"{width}x{height}")
    

    @abstractmethod
    def setTabView(self, tabViewClass: ctk.CTkTabview):
        return tabViewClass(master=self)
        