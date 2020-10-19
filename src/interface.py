# Root class
from name import Name
from region import Region
from panel import Panel


import tkinter as tk
from sumonnerinfo import SummonerInfo

class Interface(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("1000x600")
        self.s = SummonerInfo()
        self.app = ''
        self.callRegionFrame()

    def startNewWindow(self):
        self.app.destroy()
        del self.s
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

