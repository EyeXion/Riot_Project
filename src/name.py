# Frame that asks for the summoner's name

import tkinter as tk

class Name(tk.Frame):

    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.restartButton = tk.Button(self)
        self.restartButton["text"] = "RESTART"
        self.restartButton["command"] = self.master.startNewWindow
        self.restartButton["fg"] = "red"
        self.textName = tk.Label(self)
        self.inputName= tk.Entry(self)
        self.labelError = tk.Label(self)
        self.textError = tk.StringVar(self)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.textName["text"] = "Entrez votre nom d'invocateur pour la région " + self.master.s.region
        self.textName.grid(column = 0, row = 0)
        self.inputName.bind("<KeyPress-Return>", self.getName)
        self.inputName['bg'] = "cyan"
        self.inputName.grid(column = 1, row = 1)
        self.textError.set("")
        self.labelError["textvariable"] = self.textError
        self.labelError.grid(column = 0, row = 2)
        self.restartButton.grid(row = 1, column = 2, padx = 100)



    def getName(self,arg = None):
        name = self.inputName.get()
        res = self.master.s.getSummonerName(name)
        if res:
            print(self.master.s.s_info_dict)
            self.master.callPanelFrame()
        else:
            self.inputName['bg'] = 'magenta'
            self.textError.set("Erreur sur le nom d'invocateur, réessayez")