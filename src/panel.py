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

    dict_image_mastery = { 1 : "assets/mastery-1.png",
                           2: "assets/mastery-2.png",
                           3: "assets/mastery-3.png",
                           4: "assets/mastery-4.png",
                           5: "assets/mastery-5.png",
                           6: "assets/mastery-6.png",
                           7: "assets/mastery-7.png",
    }

    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.master.s.getSummonerRank()
        self.restartButton = tk.Button(self)
        self.restartButton["text"] = "RESTART"
        self.restartButton["command"] = self.master.startNewWindow
        self.restartButton["fg"] = "red"
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
        self.profileIconPath = self.master.s.getSummonerIcon()
        self.labelIcon  = tk.Label(self)
        self.master.s.getSummonerMastery()
        self.championMastery = self.master.s.s_mastery_dict
        self.labelChampionMasteryIcon = []
        self.labelChampionMasteryLevel = []
        self.labelChampionMasteryName = []
        for i in range(0,3):
            self.labelChampionMasteryIcon.append(tk.Label(self))
            self.labelChampionMasteryLevel.append(tk.Label(self))
            self.labelChampionMasteryName.append(tk.Label(self))
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.restartButton.grid(row = 0, column = 4, padx = 50)
        self.labelName["text"] = self.master.s.name
        self.labelName.config(font=("Helvetica", 40))
        self.labelLevel["text"] = "Lvl " + str(self.master.s.s_info_dict['summonerLevel'])
        self.labelLevel.config(font=("Helvetica", 40), fg='red')
        self.labelLevel.grid(row = 0, column = 2, padx = 20)
        self.labelName.grid(row = 0, column = 0, padx = 20)
        emblem = Image.open(self.dict_image_tier[self.tier])
        emblem = emblem.resize((int(emblem.size[0] * 0.3), int(emblem.size[1] * 0.3)))
        imageEmblem = ImageTk.PhotoImage(emblem)
        self.labelEmblem["image"] = imageEmblem
        self.labelEmblem.image = imageEmblem
        self.labelEmblem.grid(row = 0, column = 1, padx = 30)
        profileIcon = Image.open(self.profileIconPath)
        profileIcon = profileIcon.resize((int(profileIcon.size[0] * 0.5),int(profileIcon.size[1] * 0.5)))
        imageProfileIcon = ImageTk.PhotoImage(profileIcon)
        self.labelIcon["image"] = imageProfileIcon
        self.labelIcon.image = imageProfileIcon
        self.labelIcon.grid(row = 0, column = 3, padx = 20)
        imageMastery = []
        emblemMastery = []


        for i in range(0,3):
            try :
                idImage = self.championMastery[i]["championId"]
                masteryLevel = self.championMastery[i]["championLevel"]
                tmpEmblem = Image.open(self.dict_image_mastery[masteryLevel])
                tmpEmblem = tmpEmblem.resize((int(tmpEmblem.size[0] * 0.8),int(tmpEmblem.size[1] * 0.8)))
                emblemMastery.append(ImageTk.PhotoImage(tmpEmblem))
                tmpEmblem.close()
                self.labelChampionMasteryName[i]["text"] = self.master.s.getChampionInfo(i)["name"]
                icon_path = self.master.s.getChampionIcon(i)
                tmpImage = Image.open(icon_path)
                tmpImage = tmpImage.resize((int(tmpImage.size[0] * 0.8),int(tmpImage.size[1] * 0.8)))
                imageMastery.append(ImageTk.PhotoImage(tmpImage))
                tmpImage.close()
                self.labelChampionMasteryIcon[i]["pady"] = 40
                self.labelChampionMasteryName[i]["pady"] = 40
                self.labelChampionMasteryLevel[i]["pady"] = 40
                self.labelChampionMasteryName[i].config(font=("Helvetica", 40), fg='blue')
                self.labelChampionMasteryIcon[i]["image"] = imageMastery[i]
                self.labelChampionMasteryIcon[i].image = imageMastery[i]
                self.labelChampionMasteryLevel[i]["image"] = emblemMastery[i]
                self.labelChampionMasteryLevel[i].image = emblemMastery[i]
                self.labelChampionMasteryName[i].grid(row = i+1, column = 1)
                self.labelChampionMasteryIcon[i].grid(row = i+1, column = 2)
                self.labelChampionMasteryLevel[i].grid(row = i+1, column = 3)
            except IndexError:
                print("Index error dans l'affiche maitrise avec i = " + str(i))
                self.labelChampionMasteryLevel[i]["text"] = "VOID"
                self.labelChampionMasteryName[i]["text"] ="VOID"
                self.labelChampionMasteryIcon[i]["text"] = "VOID"
                self.labelChampionMasteryName[i].grid(row = i+1, column = 1)
                self.labelChampionMasteryIcon[i].grid(row = i+1, column = 2)
                self.labelChampionMasteryLevel[i].grid(row = i+1, column = 3)




