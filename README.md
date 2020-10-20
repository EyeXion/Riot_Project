# Riot_Project

Small app coded in Python 3.8 that displays info about LOL summoner. Uses Riot API and CommunityDragon data.

## Use it !

You will need several modules to run this. They are :

- tkinter (build-in module in theory but we never know)
- PIL (module_name : Pillow, it's a fork of the original PIL)
- requests

You can use these commands in a Unix terminal to install the latter two : 

```bash
pip3 install Pillow
pip3 install requests
```

You wont be able to use this small app if you don't have a Riot API key. If you want one, it's there : https://developer.riotgames.com/ (a developer key lasts for a day). You will need to copy/paste it `src/summonerinfo.py` line 7 (`apiKey = "<YOUR KEY>"`).
If you don't want to create an account, you can contact me and I will give you my temporary developer key that lasts for a day. 

Then you only need to run the app (the main is in `src/main.py`)

NB : This app only was created for learning and fun purposes and no other purpose whatsoever. It is kind of bad, but really fun to create ! 
