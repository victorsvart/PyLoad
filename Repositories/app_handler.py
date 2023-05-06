import customtkinter as ctk
from abc import ABC, abstractmethod
from Repositories.tableandwidget_handler import TabAndWidgetHandler

class App(ctk.CTk):
    def __init__(self, title, width, height, apperanceMode):
        self.windowName = title
        self.width = width
        self.height = height
        self.apperanceMode = apperanceMode
        super().__init__()

    @abstractmethod
    def setAppConfig(self):
        self._set_appearance_mode(f"{self.apperanceMode}")
        self.title(f"{self.windowName}")
        self.geometry(f"{self.width}x{self.height}")
    

    @abstractmethod
    def setTabView(self, tabViewClass: TabAndWidgetHandler):
        self.tabView = tabViewClass(master=self)
        self.tabView.pack(padx=20, pady=20, fill="both", expand=True)

    


        
