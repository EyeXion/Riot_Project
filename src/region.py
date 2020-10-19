# Region frame, asks for the region of the sumonner

import tkinter as tk

class Region(tk.Frame):

    regDictionnary = {0: "euw1", 1: "na1", 2: "kr", 3: "eun1", 4: "jp1"}

    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.yDefil = tk.Scrollbar(self) # Scrollbar for the ListRegion
        self.yDefil["orient"] = 'vertical'
        self.listRegion = tk.Listbox(self) # Listbox for region selection
        self.yDefil["command"] = self.listRegion.yview()
        self.textTitle = tk.Label(self)
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.textTitle["text"] = "Entrez EUW, JP, EUN ou KR pour la région"
        self.listRegion["yscrollcommand"] = self.yDefil.set(1,5)
        self.listRegion.insert(0, "EUW")
        self.listRegion.insert(1, "NA")
        self.listRegion.insert(2, "KR")
        self.listRegion.insert(3, "EUN")
        self.listRegion.insert(4, "JP")
        self.listRegion.activate(1)
        self.listRegion.bind("<KeyPress-Return>", self.getRegion)
        self.textTitle.pack()
        self.listRegion.pack()

    def getRegion(self, arg):
        index = self.listRegion.curselection()[0]
        self.master.s.region = self.regDictionnary[index]
        print("Region  : " + self.master.s.region)
        self.master.callNameFrame()



