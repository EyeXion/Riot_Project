# Root class
from src.name import Name
from src.region import Region
from src.panel import Panel


import tkinter as tk
from src.sumonnerinfo import SummonerInfo

class Interface(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("1000x600")
        self.s = SummonerInfo()
        self.app = ''
        self.callRegionFrame()

    def callRegionFrame(self):
        self.app = Region(self)
        self.app.mainloop()

    def callNameFrame(self):
        self.app.pack_forget()
        self.app.destroy()
        self.app = Name(self)
        self.app.mainloop()

    def callPanelFrame(self):
        self.app.grid_forget()
        self.app.destroy()
        self.app = Panel(self)
        self.app.mainloop()

