# Link to the RIOT API to get the needed data

import requests as r
import os

# API Key to access Riot API (dev one, needs to be changed daily)
apiKey = "RGAPI-1cbfc45d-1f75-4504-bc88-4a1f000c913c"


# Class that gets summoner info
class SummonerInfo:
    regDictionnary = {"EUW": "euw1", "NA": "na1", "KR": "kr", "EUN": "eun1", "JP": "jp1"}

    def __init__(self):
        self.s_rank_dict = {}
        self.s_info_dict = {}
        self.name = ""
        self.id = ""
        self.region = ""
        self.s_mastery_dict = ""

    # Method called to start the gathering of info
    def getInfo(self):
        #self.getRegion()
        #self.getSummonerName()
        #self.getSumonnerRank()
        pass

    # Ask for summoner Name. We get all the info about him with that (id, level, etc in s_info_dict)
    def getSummonerName(self, name):
        self.name = name
        sumonner_request = r.get("https://" + self.region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + self.name + "?api_key=" + apiKey)
        if sumonner_request.status_code == 200:
            self.s_info_dict  = sumonner_request.json()
            self.id = self.s_info_dict['id']
            return True
        else:
            print("Error")
            print(sumonner_request.json())
            return False

    # Asks for sumonner info ranked games (only returns 5*5 solo)
    def getSummonerRank(self):
        rank_request = r.get("https://" + self.region + ".api.riotgames.com/lol/league/v4/entries/by-summoner/" + self.id + "?api_key=" + apiKey)

        if rank_request.status_code == 200:
            for i in rank_request.json():
                if i["queueType"] == "RANKED_SOLO_5x5":
                    self.s_rank_dict = i
            if not rank_request.json():
                self.s_rank_dict['tier'] = "UNRANKED"
        else:
            print("Error")
            print(rank_request.json())

    def getSummonerIcon(self):
        icon_request = r.get("https://cdn.communitydragon.org/latest/profile-icon/" + str(self.s_info_dict['profileIconId']))

        if icon_request.status_code == 200:
            if os.path.exists("loadedassets/profileIcon.png"):
                os.remove("loadedassets/profileIcon.png")
            file = open("loadedassets/profileIcon.png", "wb")
            file.write(icon_request.content)
            file.close()
            return "loadedassets/profileIcon.png"
        else:
            print("Erreur chargement image profile")
            print(icon_request.status_code)

    def getSummonerMastery(self):
        mastery_request = r.get("https://" + self.region + ".api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/" + self.id + "?api_key=" + apiKey)

        if mastery_request.status_code == 200:
            self.s_mastery_dict = mastery_request.json()
            return True
        else:
            print("Error chargement maitrise champions")
            print(mastery_request.json())
            return False

    def getChampionInfo(self, index):
        info_request = r.get("https://cdn.communitydragon.org/latest/champion/" + str(self.s_mastery_dict[index]["championId"]) + "/data")

        if info_request.status_code == 200:
            return info_request.json()
        else:
            print("Error requete recherche data champion")
            print(info_request.json())
            return {}

    def getChampionIcon(self,index):
        icon_request = r.get(" https://cdn.communitydragon.org/latest/champion/" + str(self.s_mastery_dict[index]["championId"]) + "/square")

        if icon_request.status_code == 200:
            name_file = "loadedassets/championIcon" + str(index) + ".png"
            if os.path.exists(name_file):
                os.remove(name_file)
            file = open(name_file, "wb")
            file.write(icon_request.content)
            file.close()
            return name_file
        else:
            print("Error requete recherche data champion")
            print(info_request.json())
            return {}