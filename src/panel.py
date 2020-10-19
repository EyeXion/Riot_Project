# Panel with sumonner info
from PIL import Image, ImageTk

import tkinter as tk

class Panel(tk.Frame):

    dict_image_tier = {"IRON" : "assets/Emblem_Iron.png",
                       "BRONZE" : "assets/Emblem_Bronze.png",
                       "SILVER" : "assets/Emblem_Silver.png",
                       "GOLD" : "assets/Emblem_Gold.png",
                       "PLATINUM" : "assets/Emblem_Platinum.png",
                       "DIAMOND" : "assets/Emblem_Diamond.png",
                       "MASTER" : "assets/Emblem_Iron.Master",
                       "GRANDMASTER" : "assets/Emblem_Grandmaster.png",
                       "CHALLENGER" : "assets/Emblem_Challenger.png",
                       "UNRANKED" : "assets/Emblem_Challenger.png"}

    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.master.s.getSummonerRank()
        self.profileIconPath = self.master.s.getSummonerIcon()
        self.tier = self.master.s.s_rank_dict["tier"]
        try :
            self.rank = self.master.s.s_rank_dict["rank"]
            self.lp = self.master.s.s_rank_dict["leaguePoints"]
        except KeyError:
            self.rank = 0
            self.lp = 0
        self.labelName = tk.Label(self)
        self.labelEmblem = tk.Label(self)
        self.labelLevel = tk.Label(self)
        self.labelIcon  = tk.Label(self)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.labelName["text"] = self.master.s.name
        self.labelName.config(font=("Helvetica", 40))
        self.labelLevel["text"] = "Lvl " + str(self.master.s.s_info_dict['summonerLevel'])
        self.labelLevel.config(font=("Helvetica", 40), fg='red')
        self.labelLevel.grid(row = 0, column = 2)
        self.labelName.grid(row = 0, column = 0)
        emblem = Image.open(self.dict_image_tier[self.tier])
        emblem = emblem.resize((int(emblem.size[0] * 0.3), int(emblem.size[1] * 0.3)))
        imageEmblem = ImageTk.PhotoImage(emblem)
        self.labelEmblem["image"] = imageEmblem
        self.labelEmblem.image = imageEmblem
        self.labelEmblem.grid(row = 0, column = 1)
        profileIcon = Image.open(self.profileIconPath)
        profileIcon = profileIcon.resize((int(profileIcon.size[0] * 0.5),int(profileIcon.size[1] * 0.5)))
        imageProfileIcon = ImageTk.PhotoImage(profileIcon)
        self.labelIcon["image"] = imageProfileIcon
        self.labelIcon.image = imageProfileIcon
        self.labelIcon.grid(row = 1, column = 0)
