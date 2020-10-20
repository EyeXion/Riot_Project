# Region frame, asks for the region of the sumonner

import tkinter as tk

class Region(tk.Frame):

    regDictionnary = {0: "euw1", 1: "na1", 2: "kr", 3: "eun1", 4: "jp1"}

    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.errorMessage = tk.Label(self)
        self.submitButton = tk.Button(self)
        self.yDefil = tk.Scrollbar(self) # Scrollbar for the ListRegion
        self.yDefil["orient"] = 'vertical'
        self.listRegion = tk.Listbox(self) # Listbox for region selection
        self.yDefil["command"] = self.listRegion.yview()
        self.textTitle = tk.Label(self)
        self.credits = tk.Label(self)
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.submitButton["text"] = "Next"
        self.submitButton["command"] = self.getRegion
        self.submitButton["fg"] = "green"
        self.credits["text"] = "Coded by EyeXion : https://github.com/EyeXion"
        self.textTitle["text"] = "Enter EUW, JP, EUN or KR for the region"
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
        self.submitButton.pack()
        self.credits.pack(side="bottom")

    def getRegion(self, arg = None):
        try :
            index = self.listRegion.curselection()[0]
            self.master.s.region = self.regDictionnary[index]
            self.master.callNameFrame()
        except IndexError:
            self.errorMessage["text"] = "No entry selected, please select a region"
            self.errorMessage["fg"] = "red"
            self.errorMessage.config(font=("Helvetica", 20))
            self.errorMessage.pack(pady = 50)



