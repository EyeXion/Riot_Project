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
        self.submitButton = tk.Button(self)
        self.submitButton["text"] = "Next"
        self.submitButton["command"] = self.getName
        self.submitButton["fg"] = "green"
        self.textName = tk.Label(self)
        self.inputName= tk.Entry(self)
        self.labelError = tk.Label(self)
        self.textError = tk.StringVar(self)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.textName["text"] = "Enter your summoner name for the region " + self.master.s.region
        self.textName.grid(column = 0, row = 0)
        self.inputName.bind("<KeyPress-Return>", self.getName)
        self.inputName['bg'] = "cyan"
        self.inputName.grid(column = 1, row = 1)
        self.textError.set("")
        self.labelError["textvariable"] = self.textError
        self.labelError.grid(column = 0, row = 2)
        self.restartButton.grid(row = 1, column = 3, padx = 100)
        self.submitButton.grid(row = 1, column = 2, padx = 20)



    def getName(self,arg = None):
        name = self.inputName.get()
        if name == "":
            self.inputName['bg'] = 'magenta'
            self.textError.set("Error, the text input is empty")
            self.labelError["fg"] = "red"
        else:
            res = self.master.s.getSummonerName(name)
            print(res)
            if res == 200:
                print(self.master.s.s_info_dict)
                self.master.callPanelFrame()
            elif res == 403:
                self.inputName['bg'] = 'magenta'
                self.labelError["fg"] = "red"
                self.textError.set("Error, the Riot API key is not valid !\n Check out the readme on the github repo for more info.\n https://github.com/EyeXion/Riot_Project")
            elif res == 404:
                self.inputName['bg'] = 'magenta'
                self.textError.set("Error, this summonor does not exist")
                self.labelError["fg"] = "red"