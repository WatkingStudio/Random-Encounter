# ---------------------------
#   Import Libraries

# ---------------------------
import os
import sys
import json
import codecs
import random
import re
import ctypes
import time
from os import walk

codecs.BOM_UTF8
'\xef\xbb\xbf'
sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))  # point at lib folder for classes / references

#   Import your Settings class
# ---------------------------
#   [Required] Script Information
# ---------------------------
ScriptName = "Random Encounters"
Website = "https://www.twitch.tv/mr_snoblar"
Description = "Random Encounters"
Creator = "Mr_Snoblar"
Version = "1.0.0.0"

# Twitch Channel = https://www.twitch.tv/mr_snoblar

# ---------------------------
#   Define Global FilePaths
# ---------------------------
global BaseFilePath
BaseFilePath = "Services\\Scripts\\Random-Encounter\\"
global UserDataFolderPath
UserDataFolderPath = BaseFilePath + "UserData\\"
global ListFolderPath
ListFolderPath = BaseFilePath + "Lists\\"
global EncounterFolderPath
EncounterFolderPath = UserDataFolderPath + "Encounter\\"

# ---------------------------------------
# Global Filepath Variables
# ---------------------------------------
global ActiveQuestPath
ActiveQuestPath = BaseFilePath + "ActiveQuest.json"
global BodyPartFile
BodyPartFile = ListFolderPath + "bodypart.txt"
global EncounterFile
EncounterFile =  ListFolderPath + "encounter.json"
global LocationFile
LocationFile = ListFolderPath + "location.txt"
global LootDataFile
LootDataFile = ListFolderPath + "lootData.json"
global MonsterFile
MonsterFile = ListFolderPath + "monsters.txt"
global NPCFile
NPCFile = ListFolderPath + "npc.txt"
global QuestFile
QuestFile = ListFolderPath + "quests.json"
global SpellsFile
SpellsFile = ListFolderPath + "spells.txt"
global TreasureFile
TreasureFile = ListFolderPath + "treasure.txt"
global TrophyConditionFile
TrophyConditionFile = ListFolderPath + "trophy-condition.txt"
global WeaponFile
WeaponFile = ListFolderPath + "weapons.txt"
# ---------------------------------------
# Variables
# ---------------------------------------
settingsFile = os.path.join(os.path.dirname(__file__), "Settings\settings.json")
MessageBox = ctypes.windll.user32.MessageBoxW
global locationList
locationList = ["head", "body", "hands", "legs", "feet", "right", "left"]
global IsActiveQuest
IsActiveQuest = False
global QuestCurrentCountdown
QuestCurrentCountdown = 0

# ---------------------------------------
# Classes
# ---------------------------------------
class Settings:
    """" Loads settings from file if file is found if not uses default values"""

    # The 'default' variable names need to match UI_Config
    def __init__(self, settingsFile=None):
        if settingsFile and os.path.isfile(settingsFile):
            with codecs.open(settingsFile, encoding='utf-8-sig', mode='r') as f:
                self.__dict__ = json.load(f, encoding='utf-8-sig')

        else:  # set variables if no custom settings file is found,#because Encountermaxamount is an string need to make int
            self.OnlyLive = False
            self.TurnOnEncounter = True
            self.TurnOnMonster = True
            self.TurnOnCheckLevel = True
            self.TurnOnCheckTreasure = True
            self.TurnOnEquipment = True
            self.TurnOnCheckLoot = True
            self.TurnOnCheckTrophies = True
            self.TurnOnEquip = True
            self.TurnOnQuest = True
            self.TurnOnJoin = True
            self.TurnOnRebalance = True
            self.InvalidDataResponse = "{0} does not have a valid data file"
            self.GiveLootResponse = "{0} has been rewarded with a {1}"
            self.EncounterCommand = "!encounter"
            self.EncounterResponse = "{0}"
            self.EncounterCooldownResponse = "{0} encounter command is on cooldown for {1} seconds !"
            self.EncounterCooldown = 60.0
            self.MonsterCommand = "!monster"
            self.MonsterPermission = "Moderator"
            self.MonsterPermissionInfo = "Moderator"
            self.MonsterPermissionResp = "$user -> only $permission ($permissioninfo) and higher can use this command"
            self.MonsterResponse = "/me Added {0} to the monster script"
            self.MonsterCooldownResponse = "{0}; the monster command is on cooldown for {1} seconds"
            self.MonsterCooldown = 1.0
            self.CheckLevelCommand = "!level"
            self.CheckLevelResponse = "{0} level is: {1}"
            self.CheckLevelCooldownResponse = "{0} the level command is on cooldown for {1} seconds"
            self.CheckLevelCooldown = 1.0
            self.CheckTreasureCommand = "!treasure"
            self.CheckTreasureResponse = "{0} has {1} piles of treasure!"
            self.CheckTreasureCooldownResponse = "{0} the treasure command is on cooldown for {1} seconds"
            self.CheckTreasureCooldown = 60.0
            self.EquipmentCommand = "!equipment"
            self.EquipmentWhisperResponse = "{0} check your twitch inbox for your equipment info, you may need to refresh."
            self.EquipmentMessage = "{0} has the following equipped: (head) {1}, (body) {2}, (hands) {3}, (legs) {4}, (feet) {5}, (right hand) {6}, (left hand) {7}"
            self.EquipmentSpecificResponse = "{0} has a {1} equipped on their {2}"
            self.EquipmentCooldownResponse = "{0} the equipment command is on cooldown for {1} seconds"
            self.EquipmentWhisperCooldown = 60.0
            self.EquipmentChatCooldown = 300.0
            self.CheckLootCommand = "!loot"
            self.CheckLootWhisperResponse = "{0} check your twitch inbox for your loot info, you may need to refresh."
            self.CheckLootMessage = "{0} has the following loot: {1}"
            self.CheckLootCooldownResponse = "{0} the loot command is on cooldown for {1} seconds"
            self.CheckLootWhisperCooldown = 60.0
            self.CheckLootChatCooldown = 300.0
            self.CheckTrophiesCommand = "!trophies"
            self.CheckTrophiesWhisperResponse = "{0} check your twitch inbox for your trophies info, you may need to refresh."
            self.CheckTrophiesMessage = "{0} has the following trophies: {1}"
            self.CheckTrophiesCooldownResponse = "{0} the trophies command is on cooldown for {1} seconds"
            self.CheckTrophiesWhisperCooldown = 60.0
            self.CheckTrophiesChatCooldown = 300.0
            self.EquipCommand = "!equip"
            self.EquipResponseSuccess = "{0} has successfully been equipped"
            self.EquipResponseItemInvalid = "The item {0} is not a valid item"
            self.EquipResponseLocationInvalid = "The location {0} is not a valid location for a {1}"
            self.EquipResponseItemNotOwned = "You do not currently own the item '{0}' so you are not able to equip it"
            self.EquipCooldownResponse = "{0} the equip command is on cooldown for {1} seconds"
            self.EquipCooldown = 5
            self.QuestCommand = "!quest"
            self.QuestResponse = "A quest has been started to hunt down a {0}. Type '!join' in the chat to join the quest."
            self.QuestActiveMessage = "There is currently an active quest with {0} seconds left to join the questing party"
            self.QuestCountdownMessage = "You have {0} seconds to join the questing party"
            self.QuestCountdown = 60
            self.QuestPermission = "Moderator"
            self.QuestPermissionInfo = "Moderator"
            self.QuestPermissionResponse = "$user -> only $permission ($permissioninfo) and higher can use this command"
            self.QuestInvalidMonsterResponse = "Invalid Monster Named, Selecting Random Monster"
            self.QuestSuccessResponse = "The quest to slay the {0} has been successful. The questing party returns victorious!"
            self.QuestFailedResponse = "The quest to slay the {0} has failed. The questing party managed to escape with their lives but return defeated."
            self.QuestCancelResponse = "The current quest has been cancelled."
            self.QuestErrorResponse =  "There has been an error with this quest, please check the log files."
            self.JoinCommand = "!join"
            self.JoinResponseSuccess = "{0} has joined the questing party"
            self.JoinResponseNoQuest = "{0} there is currently no active quest"
            self.JoinResponseFailed = "{0} is already a member of the questing party."
            self.JoinCooldownResponse = "{0} the join command is currently on cooldown for {1} seconds"
            self.JoinCooldown = 30
            self.RebalanceCommand = "!rebalance"
            self.RebalanceResponse = "Rebalancing Complete"
            self.RebalancePermission = "Moderator"
            self.RebalancePermissionInfo = "Moderator"
            self.RebalancePermissionResp = "{0} -> only $permission ({1}) and higher can use this command"


    # ---------------------------
    #   [Optional] Reload Settings (Called when a user clicks the Save Settings button in the Chatbot UI)
    # ---------------------------

    # Reload settings on save through UI
    def ReloadSettings(self, data):
        """Reload settings on save through UI"""
        self.__dict__ = json.loads(data, encoding='utf-8-sig')

    # Save settings to files (json and js)
    def SaveSettings(self, settingsFile):
        """Save settings to files (json and js)"""
        with codecs.open(settingsFile, encoding='utf-8-sig', mode='w+') as f:
            json.dump(self.__dict__, f, encoding='utf-8-sig')
        with codecs.open(settingsFile.replace("json", "js"), encoding='utf-8-sig', mode='w+') as f:
            f.write("var settings = {0};".format(json.dumps(self.__dict__, encoding='utf-8-sig')))

class Encounter:
    encounter = ""
    exp = 0
    treasure = 0
    trophies = ""
    loot = ""

class Item:
    name = ""
    location = ""
    offence = 0
    defence = 0

# ---------------------------------------
# Functions used for user creation/modification
# ---------------------------------------

def DetermineLevel(exp):
    if exp <= 10:
        return 1
    elif exp <= 20:
        return 2
    elif exp <= 30:
        return 3
    elif exp <= 40:
        return 4
    elif exp <= 50:
        return 5
    else:
        return 6

#------------------------------------------------------------------------------------------------------------------------

def DetermineRank(level):
    if level <= 1:
        return "Grunt"
    elif level <= 2:
        return "Warrior"
    elif level <= 3:
        return "Veteran"
    elif level <= 4:
        return "Champion"
    elif level <= 5:
        return "Hero"
    else:
        return "God"

# ---------------------------------------
# Functions used in commands
# -----------------------------------------------------------------------------------------------------------------------

def AddToFile(filepath, addme):
    with open(filepath, "a") as outfile:
        json.dump(addme, outfile, indent=4)

# -----------------------------------------------------------------------------------------------------------------------

def HasPermission(data):
    #Return true if user has permission and false if the user doesn't
    if not Parent.HasPermission(data.User, MySet.MonsterPermission, MySet.PermissionInfo):
        message = MySet.MonsterPermissionResp.format(data.UserName, MySet.MonsterPermission, MySet.PermissionInfo)
        SendResp(data, message)
        return False
    return True

# -----------------------------------------------------------------------------------------------------------------------

def CheckMonsterExists(filepath, monster):
    MonsterExists = False
    if os.path.exists(filepath):
        monsterList = ReadLinesFile(filepath)
        for line in monsterList:
            if line == monster:
                MonsterExists = True
    return MonsterExists

# -----------------------------------------------------------------------------------------------------------------------

def LiveCheck():
    if MySet.OnlyLive and not Parent.IsLive():
        return False
    else:
        return True

# -----------------------------------------------------------------------------------------------------------------------

def CountLines(filepath):
    x = 0
    with codecs.open(filepath, "r", encoding="utf-8-sig") as f:
        for line in f:
            if line.strip():
                x += 1
        return x

# -----------------------------------------------------------------------------------------------------------------------

def Log(message):
    Parent.Log(ScriptName, str(message))
    return

# -----------------------------------------------------------------------------------------------------------------------

def SendMessage(message):
    return Parent.SendStreamMessage(str(message))

# -----------------------------------------------------------------------------------------------------------------------

def SendWhisper(target, message):
    return Parent.SendStreamWhisper(str(target), str(message))

# -----------------------------------------------------------------------------------------------------------------------

def ReadLineFile(Path):
    with codecs.open(Path, "r", encoding="utf-8-sig") as f:
        line = f.readline().strip("\r\n")
    return line

# -----------------------------------------------------------------------------------------------------------------------

def ReadLinesFile(Path):
    with codecs.open(Path, "r", encoding="utf-8-sig") as f:
        lines = f.read().splitlines()
    return lines

# -----------------------------------------------------------------------------------------------------------------------

def CreatePlayerPath(player):
    playerPath = EncounterFolderPath + player + ".json"
    return playerPath

# -----------------------------------------------------------------------------------------------------------------------

# ---------------------------------------
# Functions used to apply encounter results
# ---------------------------------------

def GetTrophyCondition():
    return random.choice(ReadLinesFile(TrophyConditionFile))

def FormatTrophy(trophyString, monster):
    formattedTrophy = trophyString.replace('{0}', monster)\
        .replace('{1}', GetTrophyCondition())
    return formattedTrophy.lower()

def GetRandomLoot():
    itemName = ""
    with open(LootDataFile) as json_file:
        itemList = json.load(json_file)
        randomItemNumber = Parent.GetRandom(0, len(itemList['items']))
        itemName = itemList['items'][randomItemNumber]['name']
    return itemName

def AssignLoot(lootString):
    assignedLoot = lootString.replace('{0}', GetRandomLoot())
    return assignedLoot.lower()

def IsItemLoot(lootString):
    with open(LootDataFile) as json_file:
        itemList = json.load(json_file)
        for i in itemList['items']:
            if i['name'].lower() == lootString.lower():
                return True

        return False

def GivePlayerLoot(lootString, player):
    if not lootString == "":
        playerData = ""
        playerPath = CreatePlayerPath(player)
        if os.path.exists(playerPath):
            with open(playerPath) as json_file:
                playerData = json.load(json_file)
                if IsItemLoot(lootString):
                    playerData['loot'].append(lootString)
                else:
                    playerData['trophies'].append(lootString)

        if os.path.exists(playerPath):
            os.remove(playerPath)
        SendMessage(str(MySet.GiveLootResponse.format(player, lootString)))
        AddToFile(playerPath, playerData)
    else:
        Log("LOG MESSAGE: No lootString has been given to " + player)

def ModifyPlayerExperience(value, player):
    playerPath = CreatePlayerPath(player)
    playerData = ""
    if os.path.exists(playerPath):
        with open(playerPath) as json_file:
            playerData = json.load(json_file)
            newExp = playerData['exp'] + value
            if newExp >= 0:
                playerData['exp'] = newExp

    if os.path.exists(playerPath):
        os.remove(playerPath)
    AddToFile(playerPath, playerData)

# ---------------------------------------
# Functions used for the equip command
# ---------------------------------------

#This function checks to see if the word is a location or not
def WordIsLocation(location):
    for loc in locationList:
        if location == loc:
            return True
    return False

#This function takes the name of the item and retrieves it's data from the items list
def RetrieveItem(itemName):
    item = Item()
    validItem = False
    with open(LootDataFile) as json_file:
        itemList = json.load(json_file)
        for i in itemList['items']:
            if i['name'].lower() == itemName.lower():
                validItem = True
                item.name = itemName.lower()
                item.location = i['location']
                item.offence = i['offence']
                item.defence = i['defence']
                break
    return item

# This function applies the changes required when a new item is being equipped
# It modifies the offence and defence statistics and equips the item to the correct slot
def AssignItem(userJson, item, location):
    equipment = userJson['equipment']
    loot = userJson['loot']

    oldItem = Item()
    if location == "right":
        oldItem = RetrieveItem(equipment['right hand'])
        equipment['right hand'] = item.name.lower()
    elif location == "left":
        oldItem = RetrieveItem(equipment['left hand'])
        equipment['left hand'] = item.name.lower()
    elif location == "head":
        oldItem = RetrieveItem(equipment['head'])
        equipment['head'] = item.name.lower()
    elif location == "body":
        oldItem = RetrieveItem(equipment['body'])
        equipment['body'] = item.name.lower()
    elif location == "hands":
        oldItem = RetrieveItem(equipment['hands'])
        equipment['hands'] = item.name.lower()
    elif location == "legs":
        oldItem = RetrieveItem(equipment['legs'])
        equipment['legs'] = item.name.lower()
    elif location == "feet":
        oldItem = RetrieveItem(equipment['feet'])
        equipment['feet'] = item.name.lower()

    loot.remove(item.name.lower())
    loot.append(oldItem.name.lower())

    userJson['offence'] = userJson['offence'] - oldItem.offence + item.offence
    userJson['defence'] = userJson['defence'] - oldItem.defence + item.defence
    userJson['equipment'] = equipment

    return userJson

# ---------------------------------------
# Functions used for the quest command
# ---------------------------------------

def IsCurrentlyActiveQuest():
    return IsActiveQuest

def ToggleActiveQuest():
    global IsActiveQuest
    IsActiveQuest = not IsActiveQuest

def DetermineQuestResult():
    if os.path.exists(ActiveQuestPath):
        with open(ActiveQuestPath) as json_file:
            questData = json.load(json_file)
            party = questData['Party']
            partyOffence = 0
            partyDefence = 0
            for member in party:
                memberPath = CreatePlayerPath(member)
                with open(memberPath) as json_file:
                    player = json.load(json_file)
                    partyOffence = partyOffence + player['offence'] + player['level']
                    partyDefence = partyDefence + player['defence'] + player['level']
            monster = GetQuestMonster(questData['Monster'])

            if not monster == None:
                monsterOffence = monster['offence']
                monsterDefence = monster['defence']

                # Currently this data is logged to check for quest balance
                Log(monster['name'])
                Log("Monster Offence: " + str(monsterOffence))
                Log("Monster Defence: " + str(monsterDefence))
                Log("Party Size: " + str(len(party)))
                Log("Party Offence: " + str(partyOffence))
                Log("Party Defence: " + str(partyDefence))

                difficulty = 0
                if partyOffence < monsterDefence:
                    difficulty += 1
                else:
                    difficulty -= 1
                if partyDefence < monsterOffence:
                    difficulty += 1
                else:
                    difficulty -= 1

                if QuestCalculation(difficulty):
                    QuestSuccessful(monster, party, difficulty)
                else:
                    QuestFailed(monster, party)
            else:
                Log("ERROR MESSAGE: Input monster is not valid.")
                SendMessage(MySet.QuestErrorResponse)
    else:
        Log("ERROR: Active Quest Path Missing")

def GetQuestMonster(monsterName):
    if os.path.exists(QuestFile):
        with open(QuestFile) as json_file:
            monsterList = json.load(json_file)
            for monster in monsterList['monsters']:
                val = monster['name'].lower()
                val2 = monsterName.lower()
                if val == val2:
                    return monster

def GetRandomQuestMonster():
    if os.path.exists(QuestFile):
        with open(QuestFile) as json_file:
            questMonsterList = json.load(json_file)
            monster = random.choice(questMonsterList['monsters'])
            return monster['name']

def QuestCalculation(difficulty):
    percent = random.random()

    if difficulty == -2:
        if percent > 0.17:
            return True
    elif difficulty == -1:
        if percent > 0.34:
            return True
    elif difficulty == 0:
        if percent > 0.5:
            return True
    elif difficulty == 1:
        if percent > 0.67:
            return True
    elif difficulty == 2:
        if percent > 0.84:
            return True

    return False

def QuestSuccessful(monster, party, difficulty):
    randnum = Parent.GetRandom(0, len(party))
    randomPartyMember = party[randnum]
    SendMessage(str(MySet.QuestSuccessResponse.format(monster['name'])))
    percent = random.random()

    for member in party:
        ModifyPlayerExperience(difficulty + 3, member)

    if not monster['unique'] == "":
        if percent > 0.75:
            GivePlayerLoot(monster['unique'], randomPartyMember)
        elif not monster['loot'] == "":
            GivePlayerLoot(monster['reward'], randomPartyMember)
    elif not monster['loot'] == "":
        GivePlayerLoot(monster['reward'], randomPartyMember)

def QuestFailed(monster, party):
    SendMessage(str(MySet.QuestFailedResponse.format(monster['name'])))
    for member in party:
        ModifyPlayerExperience(-1, member)

def CheckQuestMonsterExists(monsterName):
    if os.path.exists(QuestFile):
        with open(QuestFile) as json_file:
            questMonsterList = json.load(json_file)
            for monster in questMonsterList['monsters']:
                if monsterName.lower() == monster['name'].lower():
                    return True
    return False

# ---------------------------------------
# Functions used to get random string from data files
# ---------------------------------------

def GetRandomMonster():
    return random.choice(ReadLinesFile(MonsterFile))

# -----------------------------------------------------------------------------------------------------------------------

def GetRandomTime():
    return random.randint(1, 12)

# -----------------------------------------------------------------------------------------------------------------------

def GetRandomWeapon():
    return random.choice(ReadLinesFile(WeaponFile))

# -----------------------------------------------------------------------------------------------------------------------

def GetRandomSpell():
    return random.choice(ReadLinesFile(SpellsFile))

# -----------------------------------------------------------------------------------------------------------------------

def GetRandomTreasure():
    return random.choice(ReadLinesFile(TreasureFile))

# -----------------------------------------------------------------------------------------------------------------------

def GetRandomBodyPart():
    return random.choice(ReadLinesFile(BodyPartFile))

# -----------------------------------------------------------------------------------------------------------------------

def GetRandomLocation():
    return random.choice(ReadLinesFile(LocationFile))

# -----------------------------------------------------------------------------------------------------------------------

def GetRandomNPC():
    return random.choice(ReadLinesFile(NPCFile))


# ---------------------------
#   [Required] Initialize Data (Only called on load)
# ---------------------------
def Init():
    #   Create Settings Directory
    """data on Load, required function"""
    # Globals
    global MySet
    # Load in saved settings
    MySet = Settings(settingsFile)
    return

# ---------------------------
#   [Required] Execute Data / Process messages
# ---------------------------
def Execute(data):

    global userpath
    global userDataPath
    userpath = EncounterFolderPath + data.UserName + ".txt"
    # THIS VARIABLE NAME IS MISS LEADING AND SHOULD BE CHANGED COMPLETELY
    # IT SHOULDN'T BE FOR THE ENCOUNTER PATH, BUT INSTEAD FOR THE USERS DATA
    userDataPath = CreatePlayerPath(data.UserName)

    # Added in additional randomness
    random.seed(random.seed())

    # -----------------------------------------------------------------------------------------------------------------------
    #   Encounter
    # -----------------------------------------------------------------------------------------------------------------------

    if not data.IsWhisper() and data.IsChatMessage() and not data.IsFromDiscord() and data.GetParam(
            0).lower() == MySet.EncounterCommand.lower() and LiveCheck() and MySet.TurnOnEncounter:
        if not Parent.IsOnUserCooldown(ScriptName, MySet.EncounterCommand, data.User):
            # gets a random line from the encounter files
            # This is the encounter which is selected
            encounters = ReadLinesFile(EncounterFile)

            EncounterList = []
            RandomEncounter = Encounter()

            with open(EncounterFile) as json_file:
                newEncounter = json.load(json_file)
                for e in newEncounter['encounters']:
                    en = Encounter()
                    en.encounter = e['encounter']
                    en.exp = e['exp']
                    en.treasure = e['treasure']
                    en.trophies = e['trophies']
                    en.loot = e['loot']
                    EncounterList.append(en)

                randnum = Parent.GetRandom(0, len(EncounterList))
                RandomEncounter = EncounterList[randnum]

            data2 = ""

            # The next section of code goes through the encounter and replaces any variables with the appropriate data
            # {0} - Username
            # {1} - Monster One
            # {2} - Monster Two
            # {3} - Time (1-12)
            # {4} - Weapon
            # {5} - Spell
            # {6} - Treasure
            # {7} - Body Part
            # {8} - Location
            # {9} - NPC

            randomMonster = GetRandomMonster()
            randomLoot = "null"
            loot = "null"
            trophy = "null"
            if not RandomEncounter.loot == "null":
                loot = AssignLoot(RandomEncounter.loot)
            if not RandomEncounter.trophies == "null":
                trophy = FormatTrophy(RandomEncounter.trophies, randomMonster)

            formattedEncounter = RandomEncounter.encounter.replace('{0}', data.UserName)\
                .replace('{1}', randomMonster)\
                .replace('{2}', GetRandomMonster())\
                .replace('{3}', str(GetRandomTime()))\
                .replace('{4}', GetRandomWeapon())\
                .replace('{5}', GetRandomSpell())\
                .replace('{6}', loot)\
                .replace('{7}', GetRandomBodyPart())\
                .replace('{8}', GetRandomLocation())\
                .replace('{9}', GetRandomNPC())\
                .replace('{10}', trophy)

            # constructs a response message based on parameters given in SL chatbot UI
            response = MySet.EncounterResponse.format(formattedEncounter)

            #User Stats
            #{
            #   "exp": int,
            #   "level": int,
            #   "offence": int,
            #   "defence": int,
            #   "rank": string,
            #   "equipment": [string],
            #   "treasure": [string],
            #   "trophies": [string],
            #   "loot": [string]
            #}

            # If this is the first time running the encounter script, make the user a new .json file
            if not os.path.exists(userDataPath):
                create = open(userDataPath, "w+")
                create.close()
                data2 = {}
                # Add the Experience from the encounter
                data2['exp'] = RandomEncounter.exp
                # Assign a level to the user
                data2['level'] = DetermineLevel(data2['exp'])
                # Assign a rank to the user
                data2['rank'] = DetermineRank(data2['level'])
                data2['offence'] = 0
                data2['defence'] = 0
                # Assign equipment to the user
                equipment = {}
                equipment['head'] = "leather helmet"
                equipment['body'] = "cloth shirt"
                equipment['legs'] = "leather trousers"
                equipment['feet'] = "leather boots"
                equipment['hands'] = "empty"
                equipment['right hand'] = "sword"
                equipment['left hand'] = "shield"
                data2['equipment'] = equipment
                # Assign treasure to the user
                data2['treasure'] = RandomEncounter.treasure
                # Assign Trophies to the user
                data2['trophies'] = []
                if not RandomEncounter.trophies == "null":
                    data2['trophies'].append(trophy)
                # Assign Loot to the user
                data2['loot'] = []
                if not RandomEncounter.loot == "null":
                    data2['loot'].append(loot)
            # If the user already has a .json file, open it and add the new data to it
            else:
                with open(userDataPath) as json_file:
                    data2 = json.load(json_file)
                    # Add the Experience from the encounter
                    value = data2['exp'] + RandomEncounter.exp
                    if value >= 0:
                        data2['exp'] = value
                    # Update the users level
                    data2['level'] = DetermineLevel(data2['exp'])
                    # Update the users rank
                    data2['rank'] = DetermineRank(data2['level'])
                    # Add treasure to the user
                    treasureValue = data2['treasure'] + RandomEncounter.treasure
                    data2['treasure'] = treasureValue
                    # Add Trophies from the encounter
                    if not RandomEncounter.trophies == "null":
                        data2['trophies'].append(trophy)
                    # Add Loot from the encounter
                    if not RandomEncounter.loot == "null":
                        data2['loot'].append(loot)


            if os.path.exists(userDataPath):
                os.remove(userDataPath)

            AddToFile(userDataPath, data2)

            Parent.SendStreamMessage(str(response))
            Parent.AddUserCooldown(ScriptName, MySet.EncounterCommand, data.User, MySet.EncounterCooldown)

        else:
            cooldownduration = Parent.GetUserCooldownDuration(ScriptName, MySet.EncounterCommand, data.User)
            message = MySet.EncounterCooldownResponse.format(data.UserName, cooldownduration)
            Parent.SendStreamMessage(str(message))

    # -----------------------------------------------------------------------------------------------------------------------
    #   Add Monster
    # -----------------------------------------------------------------------------------------------------------------------

    if not data.IsWhisper() and data.IsChatMessage() and not data.IsFromDiscord() and data.GetParam(
            0).lower() == MySet.MonsterCommand.lower() and LiveCheck() and MySet.TurnOnMonster:

        moderator = (Parent.HasPermission(data.User, "Moderator", ""))
        if not Parent.IsOnUserCooldown(ScriptName, MySet.MonsterCommand, data.User) and moderator is True:
            monsterName = data.GetParam(1)
            monsterName = monsterName.replace('_', ' ')
            response = "NULL"
            #Add A Monster File Check
            if CheckMonsterExists(MonsterFile, monsterName):
                response = monsterName + " is already part of the monster list. Unable to add duplicate monster"
            else:
                AddToFile(MonsterFile, monsterName)

                # constructs a response message based on parameters given in SL chatbot UI
                response = MySet.MonsterResponse.format(data.GetParam(1))

            Parent.SendStreamMessage(str(response))
            Parent.AddUserCooldown(ScriptName, MySet.MonsterCommand, data.User, MySet.MonsterCooldown)
        else:
            cooldownduration = Parent.GetUserCooldownDuration(ScriptName, MySet.MonsterCommand, data.User)
            message = MySet.MonsterCooldownResponse.format(data.UserName, cooldownduration)
            Parent.SendStreamMessage(str(message))

    # -----------------------------------------------------------------------------------------------------------------------
    #   Check Level
    # -----------------------------------------------------------------------------------------------------------------------

    if not data.IsWhisper() and data.IsChatMessage() and not data.IsFromDiscord() and data.GetParam(
            0).lower() == MySet.CheckLevelCommand.lower() and LiveCheck() and MySet.TurnOnCheckLevel:
        if not Parent.IsOnUserCooldown(ScriptName, MySet.CheckLevelCommand, data.User):
            response = "null"

            if os.path.exists(userDataPath):
                with open(userDataPath) as json_file:
                    data2 = json.load(json_file)
                    response = MySet.CheckLevelResponse.format(data.UserName, data2['level'])
            else:
                response = MySet.InvalidDataResponse.format(data.UserName)

            Parent.SendStreamMessage(str(response))
            Parent.AddUserCooldown(ScriptName, MySet.CheckLevelCommand, data.User, MySet.CheckLevelCooldown)

        else:
            cooldownduration = Parent.GetUserCooldownDuration(ScriptName, MySet.CheckLevelCommand, data.User)
            message = MySet.CheckLevelCooldownResponse.format(data.UserName,cooldownduration)
            Parent.SendStreamMessage(str(message))

    # -----------------------------------------------------------------------------------------------------------------------
    #   Check Treasure
    # -----------------------------------------------------------------------------------------------------------------------

    if not data.IsWhisper() and data.IsChatMessage() and not data.IsFromDiscord() and data.GetParam(
            0).lower() == MySet.CheckTreasureCommand.lower() and LiveCheck() and MySet.TurnOnCheckTreasure:
        if not Parent.IsOnUserCooldown(ScriptName, MySet.CheckTreasureCommand, data.User):
            response = "null"

            if os.path.exists(userDataPath):
                with open(userDataPath) as json_file:
                    data2 = json.load(json_file)
                    response = MySet.CheckTreasureResponse.format(data.UserName, data2['treasure'])
            else:
                response = MySet.InvalidDataResponse.format(data.UserName)

            Parent.SendStreamMessage(str(response))
            Parent.AddUserCooldown(ScriptName, MySet.CheckTreasureCommand, data.User, MySet.CheckTreasureCooldown)

        else:
            cooldownduration = Parent.GetUserCooldownDuration(ScriptName, MySet.CheckTreasureCommand, data.User)
            message = MySet.CheckTreasureCooldownResponse.format(data.UserName,cooldownduration)
            Parent.SendStreamMessage(str(message))

    # -----------------------------------------------------------------------------------------------------------------------
    #   Check Equipment
    # -----------------------------------------------------------------------------------------------------------------------

    if not data.IsWhisper() and data.IsChatMessage() and not data.IsFromDiscord() and data.GetParam(
        0).lower() == MySet.EquipmentCommand.lower() and LiveCheck() and MySet.TurnOnEquipment:
        if not Parent.IsOnUserCooldown(ScriptName, MySet.EquipmentCommand, data.User):
            response = "null"

            # Check to see if the user wants to know what is equipped in a specific location
            if os.path.exists(userDataPath):
                with open(userDataPath) as json_file:
                    data2 = json.load(json_file)
                    equipment = data2['equipment']
                    if(data.GetParam(1).lower() == 'head' or data.GetParam(2).lower() == 'head'):
                        response = MySet.EquipmentSpecificResponse.format(data.UserName, equipment['head'], "head")
                    elif(data.GetParam(1).lower() == 'body' or data.GetParam(2).lower() == 'body'):
                        response = MySet.EquipmentSpecificResponse.format(data.UserName, equipment['body'], "body")
                    elif(data.GetParam(1).lower() == 'hands' or data.GetParam(2).lower() == 'hands'):
                        response = MySet.EquipmentSpecificResponse.format(data.UserName, equipment['hands'], "hands")
                    elif(data.GetParam(1).lower() == 'legs' or data.GetParam(2).lower() == 'legs'):
                        response = MySet.EquipmentSpecificResponse.format(data.UserName, equipment['legs'], "legs")
                    elif(data.GetParam(1).lower() == 'feet' or data.GetParam(2).lower() == 'feet'):
                        response = MySet.EquipmentSpecificResponse.format(data.UserName, equipment['feet'], "feet")
                    elif(data.GetParam(1).lower() == 'righthand' or data.GetParam(2).lower() == 'righthand'):
                        response = MySet.EquipmentSpecificResponse.format(data.UserName, equipment['right hand'], "right hand")
                    elif(data.GetParam(1).lower() == 'lefthand' or data.GetParam(2).lower() == 'lefthand'):
                        response = MySet.EquipmentSpecificResponse.format(data.UserName, equipment['left hand'], "left hand")
                    else:
                        response = MySet.EquipmentMessage.format(data.UserName, equipment['head'], equipment['body'],
                                                              equipment['hands'], equipment['legs'], equipment['feet'],
                                                              equipment['right hand'], equipment['left hand'])
            else:
                response = MySet.InvalidDataResponse.format(data.UserName)

            # Check to see if the user wants to print the information into the Twitch chat
            if(data.GetParam(1).lower() == "chat"):
                SendMessage(str(response))
                Parent.AddUserCooldown(ScriptName, MySet.EquipmentCommand, data.User, MySet.EquipmentChatCooldown)
            else:
                SendWhisper(data.UserName, str(response))
                SendMessage(str(MySet.EquipmentWhisperResponse.format(data.UserName)))
                Parent.AddUserCooldown(ScriptName, MySet.EquipmentCommand, data.User, MySet.EquipmentWhisperCooldown)

        else:
            cooldownduration = Parent.GetUserCooldownDuration(ScriptName, MySet.EquipmentCommand, data.User)
            message = MySet.EquipmentCooldownResponse.format(data.UserName, cooldownduration)
            SendMessage(str(message))

    # -----------------------------------------------------------------------------------------------------------------------
    #   Loot
    # -----------------------------------------------------------------------------------------------------------------------

    if not data.IsWhisper() and data.IsChatMessage() and not data.IsFromDiscord() and data.GetParam(
        0).lower() == MySet.CheckLootCommand.lower() and LiveCheck() and MySet.TurnOnCheckLoot:
        if not Parent.IsOnUserCooldown(ScriptName, MySet.CheckLootCommand, data.User):
            response = "null"

            if os.path.exists(userDataPath):
                with open(userDataPath) as json_file:
                    data2 = json.load(json_file)
                    loot = data2['loot']
                    response = MySet.CheckLootMessage.format(data.UserName, loot)
            else:
                response = MySet.InvaldDataResponse.format(data.UserName)

            # Check to see if the user wants to print the information into the Twitch chat
            if(data.GetParam(1).lower() == "chat"):
                SendMessage(str(response))
                Parent.AddUserCooldown(ScriptName, MySet.CheckLootCommand, data.User, MySet.CheckLootChatCooldown)
            else:
                SendWhisper(data.UserName, str(response))
                SendMessage(str(MySet.CheckLootWhisperResponse))
                Parent.AddUserCooldown(ScriptName, MySet.CheckLootCommand, data.User, MySet.CheckLootWhisperCooldown)
        else:
            cooldownduration = Parent.GetUserCooldownDuration(ScriptName, MySet.CheckLootCommand, data.User)
            message = MySet.CheckLootCooldownResponse.format(data.UserName, cooldownduration)
            SendMessage(str(message))

    # -----------------------------------------------------------------------------------------------------------------------
    #   Trophies
    # -----------------------------------------------------------------------------------------------------------------------

    if not data.IsWhisper() and data.IsChatMessage() and not data.IsFromDiscord() and data.GetParam(
        0).lower() == MySet.CheckTrophiesCommand.lower() and LiveCheck() and MySet.TurnOnCheckTrophies:
        if not Parent.IsOnUserCooldown(ScriptName, MySet.CheckTrophiesCommand, data.User):
            response = "null"

            if os.path.exists(userDataPath):
                with open(userDataPath) as json_file:
                    data2 = json.load(json_file)
                    trophies = data2['trophies']
                    response = MySet.CheckTrophiesMessage.format(data.UserName, trophies)
            else:
                response = MySet.InvalidDataResponse.format(data.UserName)

            #Check to see if the user wants to print the information into the Twitch chat
            if(data.GetParam(1).lower() == "chat"):
                SendMessage(str(response))
                Parent.AddUserCooldown(ScriptName, MySet.CheckTrophiesCommand, data.user, MySet.CheckTrophiesChatCooldown)
            else:
                SendWhisper(data.UserName, str(response))
                SendMessage(str(MySet.CheckTrophiesWhisperResponse))
                Parent.AddUserCooldown(ScriptName, MySet.CheckTrophiesCommand, data.User, MySet.CheckTrophiesWhisperCooldown)
        else:
            cooldownduration = Parent.GetUserCooldownDuration(ScriptName, MySet.CheckTrophiesCommand, data.User)
            message = MySet.CheckTrophiesCooldownResponse.format(data.UserName, cooldownduration)
            SendMessage(str(message))

    # -----------------------------------------------------------------------------------------------------------------------
    #   Equip
    # -----------------------------------------------------------------------------------------------------------------------

    if not data.IsWhisper() and data.IsChatMessage() and not data.IsFromDiscord() and data.GetParam(
            0).lower() == MySet.EquipCommand.lower() and LiveCheck() and MySet.TurnOnEquip:
        if not Parent.IsOnUserCooldown(ScriptName, MySet.EquipCommand, data.User):

            itemName = ""
            numberOfParams = data.GetParamCount()

            for i in range (1, numberOfParams):
                word = data.GetParam(i)
                if not WordIsLocation(word):
                    if i != 1:
                        itemName += " "
                    itemName += word

            item = RetrieveItem(itemName.lower())
            itemIsValid = True
            if item.name == "":
                itemIsValid = False

            if itemIsValid:
                location = data.GetParam(numberOfParams - 1).lower()
                locationIsValid = True
                itemIsOwned = False

                with open(userDataPath) as json_file:
                    data2 = json.load(json_file)

                    for i in data2['loot']:
                        if i.lower() == item.name.lower():
                            itemIsOwned = True
                            break

                    if itemIsOwned:
                        hasLocation = WordIsLocation(location)
                        # If a location is specified use that location
                        #  otherwise use the first location in the array
                        if hasLocation == True:
                            for loc in item.location:
                                if location == loc:
                                    locationIsValid = True
                                    data2 = AssignItem(data2, item, location)
                                    break
                                else:
                                    locationIsValid = False
                        else:
                            data2 = AssignItem(data2, item, item.location[0])

                # If the item and location is valid, update the users files
                if locationIsValid and itemIsOwned:
                    if os.path.exists(userDataPath):
                        os.remove(userDataPath)
                    AddToFile(userDataPath, data2)
                    Parent.AddUserCooldown(ScriptName, MySet.EquipCommand, data.User, MySet.EquipCooldown)
                    SendWhisper(data.UserName, str(MySet.EquipResponseSuccess.format(itemName)))
                elif not itemIsOwned:
                    SendWhisper(data.UserName, str(MySet.EquipResponseItemNotOwned.format(itemName)))
                else:
                    SendWhisper(data.UserName, str(MySet.EquipResponseLocationInvalid.format(location, itemName)))
            else:
                SendWhisper(data.UserName, str(MySet.EquipResponseItemInvalid.format(itemName)))
        else:
            cooldownduration = Parent.GetUserCooldownDuration(ScriptName, MySet.EquipCommand, data.User)
            message = MySet.EquipCooldownResponse.format(data.UserName, cooldownduration)
            SendMessage(str(message))

    # -----------------------------------------------------------------------------------------------------------------------
    #   Quest
    # -----------------------------------------------------------------------------------------------------------------------

    if not data.IsWhisper() and data.IsChatMessage() and not data.IsFromDiscord() and data.GetParam(
            0).lower() == MySet.QuestCommand.lower() and LiveCheck() and MySet.TurnOnQuest:
        IsModerator = (Parent.HasPermission(data.User, "Moderator", ""))
        if IsModerator is True:
            if data.GetParam(1) == "cancel":
                SendMessage(str(MySet.QuestCancelResponse))
                global IsActiveQuest
                IsActiveQuest = False
            else:
                if IsCurrentlyActiveQuest():
                    SendMessage(str(MySet.QuestActiveMessage.format(QuestCurrentCountdown)))
                else:
                    numberOfParams = data.GetParamCount()
                    monsterName = ""
                    if numberOfParams > 1:
                        for i in range(1, numberOfParams):
                            word = data.GetParam(i)
                            if i != 1:
                                monsterName += " "
                            monsterName += word
                        if not CheckQuestMonsterExists(monsterName):
                            Log(monsterName + ".")
                            SendMessage(str(MySet.QuestInvalidMonsterResponse))
                            monsterName = GetRandomQuestMonster()
                    else:
                        monsterName = GetRandomQuestMonster()

                    if os.path.exists(ActiveQuestPath):
                        with open(ActiveQuestPath) as json_file:
                            questData = json.load(json_file)
                            questData['Monster'] = monsterName
                            questData['Party'] = []
                        os.remove(ActiveQuestPath)
                        AddToFile(ActiveQuestPath, questData)

                    ToggleActiveQuest()
                    global QuestCurrentCountdown
                    QuestCurrentCountdown = MySet.QuestCountdown
                    global QuestStarted
                    QuestStarted = time.time()

                    SendMessage(str(MySet.QuestResponse.format(monsterName)))
                    SendMessage(str(MySet.QuestCountdownMessage.format(MySet.QuestCountdown)))
        else:
            SendMessage(str(MySet.QuestPermissionResponse.format(data.UserName, MySet.QuestPermissionInfo)))

    # -----------------------------------------------------------------------------------------------------------------------
    #   Join
    # -----------------------------------------------------------------------------------------------------------------------

    if not data.IsWhisper() and data.IsChatMessage() and not data.IsFromDiscord() and data.GetParam(
            0).lower() == MySet.JoinCommand.lower() and LiveCheck() and MySet.TurnOnJoin:
        if not Parent.IsOnUserCooldown(ScriptName, MySet.JoinCommand, data.User):
            #Check if there is an active quest
            if IsCurrentlyActiveQuest():
                if os.path.exists(ActiveQuestPath):
                    updateQuestFile = True
                    with open(ActiveQuestPath) as json_file:
                        questData = json.load(json_file)
                        party = questData['Party']
                        for member in party:
                            if member == data.UserName:
                                updateQuestFile = False
                                SendMessage(MySet.JoinResponseFailed.format(data.UserName))
                                break
                        if updateQuestFile:
                            SendMessage(str(MySet.JoinResponseSuccess.format(data.UserName)))
                            party.append(data.UserName)
                            questData['Party'] = party

                    if updateQuestFile:
                        os.remove(ActiveQuestPath)
                        AddToFile(ActiveQuestPath, questData)
            else:
                SendMessage(MySet.JoinResponseNoQuest.format(data.UserName))

            Parent.AddUserCooldown(ScriptName, MySet.JoinCommand, data.User, MySet.JoinCooldown)
        else:
            cooldownduration = Parent.GetUserCooldownDuration(ScriptName, MySet.JoinCommand, data.User)
            message = MySet.JoinCooldownResponse.format(data.UserName, cooldownduration)
            SendMessage(str(message))

    # -----------------------------------------------------------------------------------------------------------------------
    #   Rebalance
    # -----------------------------------------------------------------------------------------------------------------------

    if not data.IsWhisper() and data.IsChatMessage() and not data.IsFromDiscord() and data.GetParam(
           0).lower() == MySet.RebalanceCommand.lower() and LiveCheck() and MySet.TurnOnRebalance:
        IsModerator = (Parent.HasPermission(data.User, "Moderator", ""))
        if IsModerator is True:
            _, _, playerFilePaths = next(walk(EncounterFolderPath))
            for playerFilePath in playerFilePaths:
                playerPath = EncounterFolderPath + playerFilePath
                if os.path.exists(playerPath):
                    playerData = ""
                    with open(playerPath) as json_file:
                        playerData = json.load(json_file)
                        playerData['offence'] = 0
                        playerData['defence'] = 0
                        playerData['level'] = DetermineLevel(playerData['exp'])
                        playerData['rank'] = DetermineRank(playerData['level'])

                        equipment = playerData['equipment']
                        playerData['offence'] = RetrieveItem(equipment['right hand']).offence \
                                                + RetrieveItem(equipment['left hand']).offence \
                                                + RetrieveItem(equipment['hands']).offence \
                                                + RetrieveItem(equipment['body']).offence \
                                                + RetrieveItem(equipment['feet']).offence \
                                                + RetrieveItem(equipment['legs']).offence \
                                                + RetrieveItem(equipment['head']).offence
                        playerData['defence'] = RetrieveItem(equipment['right hand']).defence \
                                                + RetrieveItem(equipment['left hand']).defence \
                                                + RetrieveItem(equipment['hands']).defence \
                                                + RetrieveItem(equipment['body']).defence \
                                                + RetrieveItem(equipment['feet']).defence \
                                                + RetrieveItem(equipment['legs']).defence \
                                                + RetrieveItem(equipment['head']).defence
                    os.remove(playerPath)
                    AddToFile(playerPath, playerData)
            SendMessage(MySet.RebalanceResponse)
        else:
            SendMessage(str(MySet.RebalancePermissionResponse.format(data.UserName, MySet.RebalancePermissionInfo)))

# ---------------------------
#   [Required] Tick method (Gets called during every iteration even when there is no incoming data)
# ---------------------------
def Tick():
    if IsActiveQuest:
        if QuestStarted + MySet.QuestCountdown > time.time():
            global QuestCurrentCountdown
            QuestCurrentCountdown = (QuestStarted + MySet.QuestCountdown) - time.time()
        else:
            DetermineQuestResult()
            global IsActiveQuest
            IsActiveQuest = False
    return

