# Riot_Project

Small app coded in Python that displays info about LOL summoner. Uses Riot API and CommunityDragon data.

## Use it !

You will need several modules to run this. They are :

- tkinter
- PIL (module_name : Pillow)
- requests

You can use this command to install them.

```bash
pip install <module_name>
```

You wont be able to use this small app if you don't have a Riot API key. If you wnat one, it's there : https://developer.riotgames.com/ (a developer key lasts for a day). You will need to copy/paste it `src/summonerinfo.py` line 7 (`apiKey = "<YOUR KEY>"`).
If you don't want to create an account, you can contact me and I will give you my temporary developer key.

Then you only need to run the app (the main is in `src/main.py`)

NB : This app only was created for learning and fun purposes and no other purpose whatsoever. It is kind of bad, but really fun to create ! 
