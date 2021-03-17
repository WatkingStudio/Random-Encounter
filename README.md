# Random-Encounter  
![](https://img.shields.io/badge/Code-Python-informational?style=flat&logo=<LOGO_NAME>&logoColor=white&color=2bbc8a)
![](https://img.shields.io/badge/Platform-Twitch.tv-informational?style=flat&logo=<LOGO_NAME>&logoColor=white&color=AB56DC)
![](https://img.shields.io/badge/Program-PyCharm-informational?style=flat&logo=<LOGO_NAME>&logoColor=white&color=2B7CBC)
![](https://img.shields.io/badge/Version-1.0.0-informational?style=flat&logo=<LOGO_NAME>&logoColor=white&color=E1B445)

# Overview
A game inspired by DumpsteR_PlayeR2's Capture game. It has been modified to work as a DnD system within Twitch chat. The end goal is for users to be able to have random encounters, find loot, equip their warrior however they would like, and to go on quests with other members of chat for epic loot.

# Code
This project was written in Python27 using PyCharm and Streamlabs-Chatbot-Python_Boilerplate (which can be found here https://github.com/AnkhHeart/Streamlabs-Chatbot-Python-Boilerplate/wiki)

# Program Output
Depending on the command used within the Twitch chat the program will either send the user a private message on Twitch with the response, or it will post the response into the Twitch chat itself. Some commands allow the user to specify that they wish to have the response placed into the chat, however by default these have a higher cooldown to stop users spamming certain commands in the chat.

# How To Build/Run
## Twitch Streamer
To run this script on your stream you will need to do the following:
1) Download the project as a .zip file.
2) Download and setup Streamlabs Chatbot to run with your stream. More information on this can be found here (https://cdn.streamlabs.com/chatbot/Documentation_Twitch.pdf).
3) Install Python 2.7 on your system: https://www.python.org/ftp/python/2.7.13/python-2.7.13.msi
4) Place the project in a suitable folder. I personally store all my scripts in the "Streamlabs Chatbot\Services\Scripts" for convenience.
5) Before progressing open the .zip file and rename the folder to "Random-Encounter".
6) Navigate to your "Script" tab in the Streamlabs Chatbot. Note: Ensure that you have setup Streamlabs Chatbot and connected you Twitch account, otherwise the "Script" tab will not be visible.
7) Click the settings icon in the Script window, select Pick Folder and find the Python27.Lib folder.
8) Select import in the top right of the window.
9) Navigate to where you have stored the script, I store mine within the "Streamlabs Chatbot\Services\Scripts" folder.
10) Select the .zip of the project and click open.
11) Streamlabs Chatbot will then add the script to the scripts lists, and if you click on the script in the list view you will be able to modify and parameters you wish.
12) Now jump into your chat and test it out with the "!encounter" command. 

Note: If you are offline you will need to untick the "Only When Live" checkbox in the "General" group, otherwise it will not run.  
  
If you run into any issues don't hesitate to get in contact with me, I will help the best that I can to resolve any issues.

## Developer
To use this script as a developer you will need to do the following:
1) Download the project as a .zip file.
2) Download and setup Streamlabs Chatbot to run with your stream. More information on this can be found here (https://cdn.streamlabs.com/chatbot/Documentation_Twitch.pdf)
3) Install Python 2.7 on your system: https://www.python.org/ftp/python/2.7.13/python-2.7.13.msi
4) Place the project in a suitable folder. I personally store all my scripts in the "Streamlabs Chatbot\Services\Scripts" for convenience.
5) Before progressing open the .zip file and rename the folder to "Random-Encounter".
6) Navigate to your "Script" tab in the Streamlabs Chatbot. Note: Ensure that you have setup Streamlabs Chatbot and connected you Twitch account, otherwise the "Script" tab will not be visible.
7) Click the settings icon in the Script window, select Pick Folder and find the Python27.Lib folder
8) Select import in the top right of the window.
9) Navigate to where you have stored the script, I store mine within the "Streamlabs Chatbot\Services\Scripts" folder.
10) Select the .zip of the project and click open.
11) Streamlabs Chatbot will then add the script to the scripts lists, and if you click on the script in the list view you will be able to modify and parameters you wish.
12) Navigate back to where you stored the .zip file.
13) You will now see a new folder of the un-zipped project.
14) Open the folder and open the "EncounterScript.py" file in your preffered IDE.

Note: I use the program PyCharm to edit my python code, you should be able to use your IDE of choice but I have not tested it with any other programs. If you run into any issues please get in contact with me and I will help the best that I can to resolve any issues.

# Roadmap
* Continue to add more encounters, monsters and items to the appropriate lists.
* Create README files to explain how to modify the code to fit personal requirements.
* Create a visual representation of the script to display on stream
* Implement detailled logs to assist with debugging.

# Additional Details
N/A
