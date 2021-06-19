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
from datetime import date

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
global LogFile
LogFile = BaseFilePath + "LogFile.json"
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
            self.TurnOnStats = True
            self.TurnOnCharacterStats = True
            self.InvalidDataResponse = "{0} does not have a valid data file"
            self.GiveLootResponse = "{0} has been rewarded with a {1}"
            self.LevelledUpResponse = "{0} has levelled up to {1}"
            self.EncounterCommand = "!encounter"
            self.EncounterResponse = "{0}"
            self.EncounterCooldownResponse = "{0} encounter command is on cooldown for {1} seconds !"
            self.EncounterCooldown = 60.0
            self.MonsterCommand = "!monster"
            self.MonsterPermission = "Moderator"
            self.MonsterPermissionInfo = "Moderator"
            self.MonsterPermissionResp = "{0} -> only {1} ({2}) and higher can use this command"
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
            self.QuestDifficultyModifier = 1
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
            self.StatsCommand = "!stats"
            self.StatsResponse = "Item: {0}, Locations {1}, Offence: {2}, Defence: {3}"
            self.StatsInvalidResponse = "The item {0} is not valid."
            self.CharacterStatsCommand = "!character"
            self.CharacterStatsResponse = "{0} has the following stats: Rank ({1}), Offence ({2}), Defence ({3})"
            self.CharacterStatsCooldownResponse = "{0} the character stats command is currently on cooldown for {1} seconds"
            self.CharacterStatsCooldown = 30

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
# Functions used for the Gameplay Log File
# ---------------------------------------

def CreateGameplayLogFile():
    create = open(LogFile, "w+")
    create.close()
    data2 = {}
    data2['array'] = []
    arr = {}
    arr['date'] = date.today().strftime("%d/%m/%Y")
    arr['items'] = []
    arr['encounters'] = []
    arr['monsters'] = []
    data2['array'].append(arr)

    AddToFile(LogFile, data2)

#------------------------------------------------------------------------------------------------------------------------

# This function is used to log gameplay data. This is being used to debug and test the program. It will not be included
#   for the entire duration of the project. It is in the release version, but just to continue the testing process.
def AddLogEntry(section, data):
    logFileData = ""
    currentDate = date.today().strftime("%d/%m/%Y")

    if os.path.exists(LogFile):
        with open(LogFile) as json_file:
            logFileData = json.load(json_file)
            DataHasBeenAdded = False
            EntryIsUnique = True

            for logEntry in logFileData['array']:
                if logEntry['date'] == currentDate:
                    if section == "monsters":
                        for monsterEntry in logEntry['monsters']:
                            if monsterEntry['name'] == data:
                                EntryIsUnique = False
                                monsterEntry['value'] = monsterEntry['value'] + 1
                                break
                        if EntryIsUnique:
                            monster = {}
                            monster['name'] = data
                            monster['value'] = 0
                            logEntry['monsters'].append(monster)

                    elif section == "items":
                        for itemEntry in logEntry['items']:
                            if itemEntry['name'] == data:
                                EntryIsUnique = False
                                itemEntry['value'] = itemEntry['value'] + 1
                                break
                        if EntryIsUnique:
                            item = {}
                            item['name'] = data
                            item['value'] = 0
                            logEntry['items'].append(item)

                    elif section == "encounters":
                        for encounterEntry in logEntry['encounters']:
                            if encounterEntry['name'] == data:
                                EntryIsUnique = False
                                encounterEntry['value'] = encounterEntry['value'] + 1
                                break
                        if EntryIsUnique:
                            encounter = {}
                            encounter['name'] = data
                            encounter['value'] = 0
                            logEntry['encounters'].append(encounter)

                    DataHasBeenAdded = True
                    break

            if not DataHasBeenAdded:
                arr = {}
                arr['date'] = currentDate
                arr['items'] = []
                arr['monsters'] = []
                arr['encounters'] = []
                if section == "items":
                    item = {}
                    item['name'] = data
                    item['value'] = 0
                    arr['items'].append(item)
                elif section == "monsters":
                    monster = {}
                    monster['name'] = data
                    monster['value'] = 0
                    Log(arr)
                    arr['monsters'].append(monster)
                elif section == "encounters":
                    encounter = {}
                    encounter['name'] = data
                    encounter['value'] = 0
                    arr['encounters'].append(encounter)
                logFileData['array'].append(arr)

        AddToFile(LogFile, logFileData)
    else:
        Log("Log File Is Missing")

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

#------------------------------------------------------------------------------------------------------------------------

def CreatePlayer(userDataPath):
    if not os.path.exists(userDataPath):
        try:
            create = open(userDataPath, "w+")
            create.close()

            data2 = {}
            # Add the Experience from the encounter
            data2['exp'] = 0
            # Assign a level to the user
            data2['level'] = DetermineLevel(data2['exp'])
            # Assign a rank to the user
            data2['rank'] = DetermineRank(data2['level'])
            # Assign default stats to the user
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
            # Assign default items to the user
            data2['treasure'] = 0
            data2['trophies'] = []
            data2['loot'] = []

            AddToFile(userDataPath, data2)
        except:
            Log("Unable to create player file: ", userDataPath)
            return

# ---------------------------------------
# Functions used in commands
# -----------------------------------------------------------------------------------------------------------------------

def AddToFile(filepath, addme):
    with open(filepath, "w") as outfile:
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

def CheckMonsterExists(monster):
    MonsterExists = False
    for line in MonsterList:
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

# ---------------------------------------
# Functions used to apply encounter results
# ---------------------------------------

def GetTrophyCondition():
    fileLines = ReadLinesFile(TrophyConditionFile)
    index = Parent.GetRandom(0, len(fileLines))
    return fileLines[index]

#------------------------------------------------------------------------------------------------------------------------

def FormatTrophy(trophyString, monster):
    formattedTrophy = trophyString.replace('{0}', monster)\
        .replace('{1}', GetTrophyCondition())
    return formattedTrophy.lower()

#------------------------------------------------------------------------------------------------------------------------

def GetRandomLoot():
    itemName = ""
    randomItemNumber = Parent.GetRandom(0, len(LootItemList['items']))
    itemName = LootItemList['items'][randomItemNumber]['name']
    return itemName

#------------------------------------------------------------------------------------------------------------------------

def AssignLoot(lootString):
    assignedLoot = lootString.replace('{0}', GetRandomLoot())
    return assignedLoot.lower()

#------------------------------------------------------------------------------------------------------------------------

def IsItemLoot(lootString):
    for i in LootItemList['items']:
        if i['name'].lower() == lootString.lower():
            return True

    return False

#------------------------------------------------------------------------------------------------------------------------

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

        AddLogEntry("items", lootString)
        SendMessage(str(MySet.GiveLootResponse.format(player, lootString)))
        AddToFile(playerPath, playerData)
    else:
        Log("LOG MESSAGE: No lootString has been given to " + player)

#------------------------------------------------------------------------------------------------------------------------

def ModifyPlayerExperience(value, player):
    playerPath = CreatePlayerPath(player)
    playerData = ""
    if os.path.exists(playerPath):
        with open(playerPath) as json_file:
            playerData = json.load(json_file)
            newExp = playerData['exp'] + value
            if newExp >= 0:
                playerData['exp'] = newExp
            playerData['level'] = DetermineLevel(playerData['exp'])
            playerData['rank'] = DetermineRank(playerData['level'])

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

#------------------------------------------------------------------------------------------------------------------------

#This function takes the name of the item and retrieves it's data from the items list
def RetrieveItem(itemName):
    item = Item()
    validItem = False
    for i in LootItemList['items']:
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
    if not oldItem == "":
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

#------------------------------------------------------------------------------------------------------------------------

def ToggleActiveQuest():
    global IsActiveQuest
    IsActiveQuest = not IsActiveQuest

#------------------------------------------------------------------------------------------------------------------------

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
                monsterOffence = monster['offence'] * float(MySet.QuestDifficultyModifier)
                monsterDefence = monster['defence'] * float(MySet.QuestDifficultyModifier)

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

#------------------------------------------------------------------------------------------------------------------------

def GetQuestMonster(monsterName):
    for monster in QuestMonsterList['monsters']:
        val = monster['name'].lower()
        if val == monsterName.lower():
            return monster

#------------------------------------------------------------------------------------------------------------------------

def GetRandomQuestMonster():
    index = Parent.GetRandom(0, len(QuestMonsterList['monsters']))
    monster = QuestMonsterList['monsters'][index]
    return monster['name']

#------------------------------------------------------------------------------------------------------------------------

def QuestCalculation(difficulty):
    percent = Parent.GetRandom(0, 100)
    Log(percent)

    if difficulty == -2:
        if percent > 17:
            return True
    elif difficulty == -1:
        if percent > 34:
            return True
    elif difficulty == 0:
        if percent > 50:
            return True
    elif difficulty == 1:
        if percent > 67:
            return True
    elif difficulty == 2:
        if percent > 84:
            return True

    return False

#------------------------------------------------------------------------------------------------------------------------

def QuestSuccessful(monster, party, difficulty):
    SendMessage(str(MySet.QuestSuccessResponse.format(monster['name'])))
    percent = Parent.GetRandom(0, 100)

    for member in party:
        ModifyPlayerExperience(difficulty + 3, member)

    try:
        if not monster['unique'] == "null":
            randomPartyMember = party[Parent.GetRandom(0, len(party))]
            GivePlayerLoot(monster['unique'], randomPartyMember)

        numberAwarded = Parent.GetRandom(0, len(party))
        for x in range(numberAwarded + 1):
            randMember = party[Parent.GetRandom(0, len(party))]
            if not monster['reward'] == "null":
                GivePlayerLoot(monster['reward'], randMember)
            else:
                GivePlayerLoot(GetRandomLoot(), randMember)
            party.remove(randMember)

    except:
        Log("Unable to assign players loot")

#------------------------------------------------------------------------------------------------------------------------

def QuestFailed(monster, party):
    SendMessage(str(MySet.QuestFailedResponse.format(monster['name'])))
    for member in party:
        ModifyPlayerExperience(-1, member)

#------------------------------------------------------------------------------------------------------------------------

def CheckQuestMonsterExists(monsterName):
    for monster in QuestMonsterList['monsters']:
        if monsterName.lower() == monster['name'].lower():
            return True
    return False

# ---------------------------------------
# Functions used to get random string from data files
# ---------------------------------------

def GetRandomMonster():
    index = Parent.GetRandom(0, len(MonsterList))
    return MonsterList[index]

# -----------------------------------------------------------------------------------------------------------------------

def GetRandomTime():
    return Parent.GetRandom(1, 12)

# -----------------------------------------------------------------------------------------------------------------------

def GetRandomWeapon():
    index = Parent.GetRandom(0, len(RandomWeaponList))
    return RandomWeaponList[index]

# -----------------------------------------------------------------------------------------------------------------------

def GetRandomSpell():
    index = Parent.GetRandom(0, len(RandomSpellList))
    return RandomSpellList[index]

# -----------------------------------------------------------------------------------------------------------------------

def GetRandomTreasure():
    index = Parent.GetRandom(0, len(RandomTreasureList))
    return RandomTreasureList[index]

# -----------------------------------------------------------------------------------------------------------------------

def GetRandomBodyPart():
    index = Parent.GetRandom(0, len(RandomBodyPartList))
    return RandomBodyPartList[index]

# -----------------------------------------------------------------------------------------------------------------------

def GetRandomLocation():
    index = Parent.GetRandom(0, len(RandomLocationList))
    return RandomLocationList[index]

# -----------------------------------------------------------------------------------------------------------------------

def GetRandomNPC():
    index = Parent.GetRandom(0, len(RandomNpcList))
    return RandomNpcList[index]


# ---------------------------
#   [Required] Initialize Data (Only called on load)
# ---------------------------
def Init():
    #   Create Settings Directory
    """data on Load, required function"""
    # Globals
    global MySet
    global EncounterList
    global MonsterList
    global LootItemList
    global QuestMonsterList
    global RandomWeaponList
    global RandomSpellList
    global RandomTreasureList
    global RandomBodyPartList
    global RandomLocationList
    global RandomNpcList

    # Load in saved settings
    MySet = Settings(settingsFile)
    EncounterList = []
    MonsterList = []
    LootItemList = []
    QuestMonsterList = []

    RandomWeaponList = []
    RandomSpellList = []
    RandomTreasureList = []
    RandomBodyPartList = []
    RandomLocationList = []
    RandomNpcList = []

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

    if not os.path.exists(LogFile):
        CreateGameplayLogFile()

    if not os.path.exists(EncounterFolderPath):
        os.makedirs(EncounterFolderPath)

    if os.path.exists(MonsterFile):
        MonsterList = ReadLinesFile(MonsterFile)
    else:
        Log("ERROR: Monster List doesn't exist!")

    if os.path.exists(LootDataFile):
        with open(LootDataFile) as json_file:
            LootItemList = json.load(json_file)
    else:
        Log("ERROR: Loot List doesn't exist!")

    if os.path.exists(QuestFile):
        with open(QuestFile) as json_file:
            QuestMonsterList = json.load(json_file)
    else:
        Log("ERROR: Quest File doesn't exist!")

    if os.path.exists(WeaponFile):
        RandomWeaponList = ReadLinesFile(WeaponFile)
    else:
        Log("ERROR: Weapon File doesn't exist!")

    if os.path.exists(SpellsFile):
        RandomSpellList = ReadLinesFile(SpellsFile)
    else:
        Log("ERROR: Spells File doesn't exist!")

    if os.path.exists(TreasureFile):
        RandomTreasureList = ReadLinesFile(TreasureFile)
    else:
        Log("ERROR: Treasure File doesn't exist!")

    if os.path.exists(BodyPartFile):
        RandomBodyPartList = ReadLinesFile(BodyPartFile)
    else:
        Log("ERROR: Body Part doesn't exist!")

    if os.path.exists(LocationFile):
        RandomLocationList = ReadLinesFile(LocationFile)
    else:
        Log("ERROR: Location File doesn't exist!")

    if os.path.exists(NPCFile):
        RandomNpcList = ReadLinesFile(NPCFile)
    else:
        Log("ERROR: NPC File doesn't exist!")

    return

# ---------------------------
#   [Required] Execute Data / Process messages
# ---------------------------
def Execute(data):

    global userDataPath
    userDataPath = CreatePlayerPath(data.UserName)
    IsOwner = (Parent.HasPermission(data.User, "Owner", ""))

    # -----------------------------------------------------------------------------------------------------------------------
    #   Encounter
    # -----------------------------------------------------------------------------------------------------------------------

    if MySet.TurnOnEncounter and LiveCheck() and data.GetParam(0).lower() == MySet.EncounterCommand.lower() and (data.IsChatMessage() and not data.IsWhisper()):
        if IsOwner or not Parent.IsOnUserCooldown(ScriptName, MySet.EncounterCommand, data.User):

            # If this is the first time running the encounter script, make the user a new .json file
            if not os.path.exists(userDataPath):
                CreatePlayer(userDataPath)

            RandomEncounter = Encounter()
            randnum = Parent.GetRandom(0, len(EncounterList))
            RandomEncounter = EncounterList[randnum]

            AddLogEntry("encounters", RandomEncounter.encounter)
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
            AddLogEntry("monsters", randomMonster)
            randomLoot = "null"
            loot = "null"
            trophy = "null"

            if not RandomEncounter.loot == "null":
                loot = AssignLoot(RandomEncounter.loot)
                AddLogEntry("items", loot)
            if not RandomEncounter.trophies == "null":
                trophy = FormatTrophy(RandomEncounter.trophies, randomMonster)
                AddLogEntry("items", trophy)

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
            
            CurrentLevel = 0

            with open(userDataPath) as json_file:
                data2 = json.load(json_file)
                # Add the Experience from the encounter
                value = data2['exp'] + RandomEncounter.exp
                if value >= 0:
                    data2['exp'] = value
                # Update the users level
                CurrentLevel = data2['level']
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

            if CurrentLevel < data2['level']:
                SendMessage(MySet.LevelledUpResponse.format(data.UserName, data2['level']))

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

    if MySet.TurnOnMonster and LiveCheck() and data.GetParam(0).lower() == MySet.MonsterCommand.lower() and (data.IsChatMessage() and not data.IsWhisper()):
        if Parent.HasPermission(data.User, MySet.MonsterPermission, ""):
            if IsOwner or not Parent.IsOnUserCooldown(ScriptName, MySet.MonsterCommand, data.User):
                monsterName = data.GetParam(1)
                monsterName = monsterName.replace('_', ' ')
                response = "NULL"
                #Add A Monster File Check
                if CheckMonsterExists(monsterName):
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
        else:
            SendMessage(str(MySet.MonsterPermissionResp.format(data.User, MySet.MonsterPermission, MySet.MonsterPermissionInfo)))

    # -----------------------------------------------------------------------------------------------------------------------
    #   Check Level
    # -----------------------------------------------------------------------------------------------------------------------

    if MySet.TurnOnCheckLevel and LiveCheck() and data.GetParam(0).lower() == MySet.CheckLevelCommand.lower() and (data.IsChatMessage() or data.IsWhisper()):
        if IsOwner or not Parent.IsOnUserCooldown(ScriptName, MySet.CheckLevelCommand, data.User):
            response = "null"

            if os.path.exists(userDataPath):
                with open(userDataPath) as json_file:
                    data2 = json.load(json_file)
                    response = MySet.CheckLevelResponse.format(data.UserName, data2['level'])
            else:
                response = MySet.InvalidDataResponse.format(data.UserName)

            if data.IsWhisper():
                SendWhisper(data.UserName,str(response))
            else:
                SendMessage(str(response))
                Parent.AddUserCooldown(ScriptName, MySet.CheckLevelCommand, data.User, MySet.CheckLevelCooldown)

        else:
            cooldownduration = Parent.GetUserCooldownDuration(ScriptName, MySet.CheckLevelCommand, data.User)
            message = MySet.CheckLevelCooldownResponse.format(data.UserName,cooldownduration)
            SendMessage(str(message))

    # -----------------------------------------------------------------------------------------------------------------------
    #   Check Treasure
    # -----------------------------------------------------------------------------------------------------------------------

    if MySet.TurnOnCheckTreasure and LiveCheck() and data.GetParam(0).lower() == MySet.CheckTreasureCommand.lower() and (data.IsChatMessage() or data.IsWhisper()):
        if IsOwner or not Parent.IsOnUserCooldown(ScriptName, MySet.CheckTreasureCommand, data.User):
            response = "null"

            if os.path.exists(userDataPath):
                with open(userDataPath) as json_file:
                    data2 = json.load(json_file)
                    response = MySet.CheckTreasureResponse.format(data.UserName, data2['treasure'])
            else:
                response = MySet.InvalidDataResponse.format(data.UserName)

            if data.IsWhisper():
                SendWhisper(data.UserName, str(response))
            else:
                SendMessage(str(response))
                Parent.AddUserCooldown(ScriptName, MySet.CheckTreasureCommand, data.User, MySet.CheckTreasureCooldown)

        else:
            cooldownduration = Parent.GetUserCooldownDuration(ScriptName, MySet.CheckTreasureCommand, data.User)
            message = MySet.CheckTreasureCooldownResponse.format(data.UserName,cooldownduration)
            SendMessage(str(message))

    # -----------------------------------------------------------------------------------------------------------------------
    #   Check Equipment
    # -----------------------------------------------------------------------------------------------------------------------

    if MySet.TurnOnEquipment and LiveCheck() and data.GetParam(0).lower() == MySet.EquipmentCommand.lower() and (data.IsChatMessage() or data.IsWhisper()):
        if IsOwner or not Parent.IsOnUserCooldown(ScriptName, MySet.EquipmentCommand, data.User):
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
                if not data.IsWhisper():
                    Parent.AddUserCooldown(ScriptName, MySet.EquipmentCommand, data.User, MySet.EquipmentChatCooldown)
            else:
                SendWhisper(data.UserName, str(response))
                if not data.IsWhisper():
                    SendMessage(str(MySet.EquipmentWhisperResponse.format(data.UserName)))
                    Parent.AddUserCooldown(ScriptName, MySet.EquipmentCommand, data.User, MySet.EquipmentWhisperCooldown)

        else:
            cooldownduration = Parent.GetUserCooldownDuration(ScriptName, MySet.EquipmentCommand, data.User)
            message = MySet.EquipmentCooldownResponse.format(data.UserName, cooldownduration)
            SendMessage(str(message))

    # -----------------------------------------------------------------------------------------------------------------------
    #   Loot
    # -----------------------------------------------------------------------------------------------------------------------

    if MySet.TurnOnCheckLoot and LiveCheck() and data.GetParam(0).lower() == MySet.CheckLootCommand.lower() and (data.IsChatMessage() or data.IsWhisper()):
        if IsOwner or not Parent.IsOnUserCooldown(ScriptName, MySet.CheckLootCommand, data.User):
            response = "null"

            if os.path.exists(userDataPath):
                with open(userDataPath) as json_file:
                    data2 = json.load(json_file)
                    loot = data2['loot']
                    response = MySet.CheckLootMessage.format(data.UserName, loot)
            else:
                response = MySet.InvalidDataResponse.format(data.UserName)

            # Check to see if the user wants to print the information into the Twitch chat
            if(data.GetParam(1).lower() == "chat"):
                SendMessage(str(response))
                if not data.IsWhisper():
                    Parent.AddUserCooldown(ScriptName, MySet.CheckLootCommand, data.User, MySet.CheckLootChatCooldown)
            else:
                SendWhisper(data.UserName, str(response))
                if not data.IsWhisper():
                    SendMessage(str(MySet.CheckLootWhisperResponse.format(data.UserName)))
                    Parent.AddUserCooldown(ScriptName, MySet.CheckLootCommand, data.User, MySet.CheckLootWhisperCooldown)
        else:
            cooldownduration = Parent.GetUserCooldownDuration(ScriptName, MySet.CheckLootCommand, data.User)
            message = MySet.CheckLootCooldownResponse.format(data.UserName, cooldownduration)
            SendMessage(str(message))

    # -----------------------------------------------------------------------------------------------------------------------
    #   Trophies
    # -----------------------------------------------------------------------------------------------------------------------

    if MySet.TurnOnCheckTrophies and LiveCheck() and data.GetParam(0).lower() == MySet.CheckTrophiesCommand.lower() and (data.IsChatMessage() or data.IsWhisper()):
        if IsOwner or not Parent.IsOnUserCooldown(ScriptName, MySet.CheckTrophiesCommand, data.User):
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
                if not data.IsWhisper():
                    Parent.AddUserCooldown(ScriptName, MySet.CheckTrophiesCommand, data.user, MySet.CheckTrophiesChatCooldown)
            else:
                SendWhisper(data.UserName, str(response))
                if not data.IsWhisper():
                    SendMessage(str(MySet.CheckTrophiesWhisperResponse))
                    Parent.AddUserCooldown(ScriptName, MySet.CheckTrophiesCommand, data.User, MySet.CheckTrophiesWhisperCooldown)
        else:
            cooldownduration = Parent.GetUserCooldownDuration(ScriptName, MySet.CheckTrophiesCommand, data.User)
            message = MySet.CheckTrophiesCooldownResponse.format(data.UserName, cooldownduration)
            SendMessage(str(message))

    # -----------------------------------------------------------------------------------------------------------------------
    #   Equip
    # -----------------------------------------------------------------------------------------------------------------------

    if MySet.TurnOnEquip and LiveCheck() and data.GetParam(0).lower() == MySet.EquipCommand.lower() and (data.IsChatMessage() or data.IsWhisper()):
        if IsOwner or not Parent.IsOnUserCooldown(ScriptName, MySet.EquipCommand, data.User):
            if os.path.exists(userDataPath):
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
                        AddToFile(userDataPath, data2)
                        if not data.IsWhisper():
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

    if MySet.TurnOnQuest and LiveCheck() and data.GetParam(0).lower() == MySet.QuestCommand.lower() and (data.IsChatMessage() and not data.IsWhisper()):
        if Parent.HasPermission(data.User, MySet.QuestPermission, ""):
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

                    AddLogEntry("monsters", monsterName)

                    if os.path.exists(ActiveQuestPath):
                        with open(ActiveQuestPath) as json_file:
                            questData = json.load(json_file)
                            questData['Monster'] = monsterName
                            questData['Party'] = []
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

    if MySet.TurnOnJoin and LiveCheck() and data.GetParam(0).lower() == MySet.JoinCommand.lower() and (data.IsChatMessage() and not data.IsWhisper()):
        if not Parent.IsOnUserCooldown(ScriptName, MySet.JoinCommand, data.User):
            # If this is the first time running the encounter script, make the user a new .json file
            if not os.path.exists(userDataPath):
                CreatePlayer(userDataPath)

            # Check if there is an active quest
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

    if MySet.TurnOnRebalance and LiveCheck() and data.GetParam(0).lower() == MySet.RebalanceCommand.lower() and (data.IsChatMessage() and not data.IsWhisper()):
        if Parent.HasPermission(data.User, MySet.RebalancePermission, ""):
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
                    AddToFile(playerPath, playerData)
            SendMessage(MySet.RebalanceResponse)
        else:
            SendMessage(str(MySet.RebalancePermissionResp.format(data.UserName, MySet.RebalancePermission, MySet.RebalancePermissionInfo)))

    # -----------------------------------------------------------------------------------------------------------------------
    #   Stats
    # -----------------------------------------------------------------------------------------------------------------------

    if MySet.TurnOnStats and LiveCheck() and data.GetParam(0).lower() == MySet.StatsCommand.lower() and (data.IsChatMessage() or data.IsWhisper()):
        itemName = ""
        numberOfParams = data.GetParamCount()

        for i in range(1, numberOfParams):
            word = data.GetParam(i)
            if i != 1:
                itemName += " "
            itemName += word

        item = RetrieveItem(itemName.lower())
        itemIsValid = True
        if item.name == "":
            itemIsValid = False

        if itemIsValid:
            SendWhisper(data.UserName, str(MySet.StatsResponse.format(itemName, item.location, item.offence, item.defence)))
        else:
            SendWhisper(data.UserName, str(MySet.StatsInvalidResponse.format(itemName)))

    # -----------------------------------------------------------------------------------------------------------------------
    #   Character Stats
    # -----------------------------------------------------------------------------------------------------------------------

    if MySet.TurnOnCharacterStats and LiveCheck() and data.GetParam(0).lower() == MySet.CharacterStatsCommand.lower() and (data.IsChatMessage() or data.IsWhisper()):
        if not Parent.IsOnUserCooldown(ScriptName, MySet.CharacterStatsCommand, data.User):
            response = ""
            if os.path.exists(userDataPath):
                with open(userDataPath) as json_file:
                    data2 = json.load(json_file)
                    response = MySet.CharacterStatsResponse.format(data.UserName, data2['rank'], data2['offence'], data2['defence'])
            else:
                response = MySet.InvalidDataResponse.format(data.UserName)

            if data.IsWhisper():
                SendWhisper(data.UserName, response)
            else:
                SendMessage(response)
                Parent.AddUserCooldown(ScriptName, MySet.CharacterStatsCommand, data.User, MySet.CharacterStatsCooldown)
        else:
            cooldownduration = Parent.GetUserCooldownDuration(ScriptName, MySet.CharacterStatsCommand, data.User)
            message = MySet.CharacterStatsCooldownResponse.format(data.UserName, cooldownduration)
            SendMessage(str(message))

# ---------------------------
#   [Required] Tick method (Gets called during every iteration even when there is no incoming data)
# ---------------------------
def Tick():
    if IsActiveQuest:
        if QuestStarted + MySet.QuestCountdown > time.time():
            global QuestCurrentCountdown
            QuestCurrentCountdown = (QuestStarted + MySet.QuestCountdown) - time.time()
        else:
            global IsActiveQuest
            IsActiveQuest = False
            DetermineQuestResult()
    return

