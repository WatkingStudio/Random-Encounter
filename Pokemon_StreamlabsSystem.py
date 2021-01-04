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

codecs.BOM_UTF8
'\xef\xbb\xbf'
sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))  # point at lib folder for classes / references

#   Import your Settings class
# ---------------------------
#   [Required] Script Information
# ---------------------------
ScriptName = "Fantasy Encounters"
Website = "https://www.twitch.tv/mr_snoblar"
Description = "Temporary Fantasy Encounters"
Creator = "Mr_Snoblar"
Version = "1.0.0.0"

# Twitch Channel = twitch.tv/dumpster_player2

# ---------------------------
#   Define Global Variables
# ---------------------------
global FilePath
FilePath = "Services\\Scripts\\CaptureGame\\UserData\\"
global UsersMonFolder
UsersMonFolder = FilePath + "UserMon\\"
global UsersMonLevelsFolder
UsersMonLevelsFolder = FilePath + "UserMonLevels\\"
global OpenTradesFolder
OpenTradesFolder = FilePath + "OpenTrades\\"
global OpenTradesFolder
EncounterFolder = FilePath + "Encounter\\"
global PointsFolder
PointsFolder = FilePath + "Points\\"
global OpenDuelsFolder
OpenDuelsFolder = FilePath + "OpenDuels\\"
# ---------------------------------------
# Global Filepath Variables
# ---------------------------------------
global BodyPartFile
BodyPartFile = FilePath + "bodypart.txt"
global EncounterFile
EncounterFile =  FilePath + "encounter.json"
global LocationFile
LocationFile = FilePath + "location.txt"
global MonsterFile
MonsterFile = FilePath + "monsters.txt"
global NPCFile
NPCFile = FilePath + "npc.txt"
global SpellsFile
SpellsFile = FilePath + "spells.txt"
global TreasureFile
TreasureFile = FilePath + "treasure.txt"
global WeaponFile
WeaponFile = FilePath + "weapons.txt"
# ---------------------------------------
# Variables
# ---------------------------------------
settingsFile = os.path.join(os.path.dirname(__file__), "Settings\settings.json")
MessageBox = ctypes.windll.user32.MessageBoxW

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
            self.TurnOnCatch = True
            self.TurnOnBattle = True
            self.TurnOnRelease = True
            self.TurnOnTrade = True
            self.TurnOnAcceptTrade = True
            self.TurnOnRefuse = True
            self.TurnOnDuel = True
            self.TurnOnAcceptDuel = True
            self.PointsName = "Street Rep"
            self.EncounterCommand = "!encounter"
            self.EncounterResponse = "caught pokemon"
            self.EncounterCooldownResponse = "{0}, the encounter command on cooldown for {1}"
            self.EncounterNumber = 5
            self.EncounterCooldown = 60.0
            self.MonsterCommand = "!monster"
            self.MonsterPermission = "Moderator"
            self.MonsterPermissionInfo = "Moderator"
            self.MonsterPermissionResp = "$user -> only $permission ($permissioninfo) and higher can use this command"
            self.MonsterResponse = "/me Added {0} to the monster script"
            self.MonsterCooldownResponse = "{0}; the monster command is on cooldown for {1} seconds"
            self.MonsterCooldown = 1.0
            self.BattleCommand = "!battle"
            self.BattleResponse = "{0} {1} {2} {3}"
            self.BattleCooldownResponse = "Battle command is on cooldown"
            self.BattleWinChance = 50.0
            self.BattleDeathChance = "0.1"
            self.BattlePointsWin = 10
            self.BattlePointsLoss = 10
            self.BattleMaxLevel = 100
            self.BattleCooldown = 60.0
            self.ReleaseCommand = "!release"
            self.ReleaseResponse = "released {1}"
            self.ReleaseFailedResponse = "does not have a {1}"
            self.ReleaseOnCooldownResponse = "{0} the release command is on cooldown for {1} seconds"
            self.ReleaseCooldown = 60.0
            self.TradeCommand = "!trade"
            self.TradeResponse = "Trade Successful"
            self.TradeUserNotThatMonResponse = "{0} does not have a "
            self.TradeOnCooldownResponse = "{0} the trade command is on cooldown for {1} seconds"
            self.TradeCooldown = 60.0
            self.AcceptTradeCommand = "!accepttrade"
            self.AcceptTradeResponse = "{0} has accepted their trade with {1}"
            self.AcceptTradeMissingMonResponse = "{0} doesn't have a {1}"
            self.AcceptTradeNoTradeFoundResponse = "{0} and {1} doesn't have an trade pending"
            self.AcceptTradeOnCooldownResponse = "{0} the accepttrade command is on cooldown for {1} seconds"
            self.AcceptTradeCooldown = 60.0
            self.RefuseCommand = "!refuse"
            self.RefuseResponse = "{0} refused to trade with {1}"
            self.RefuseNotFoundResponse = "{0} and {1} doesn't have an trade pending"
            self.RefuseCooldownResponse = "{0} the refuse command is on cooldown for {1} seconds"
            self.RefuseCooldown = 60.0
            self.CatchCommand = "!catch"
            self.CatchResponse = "{0} {1} {2}"
            self.CatchNotFoundresponse = "{0} didnt encounter a {1}"
            self.CatchCooldownResponse = "{0} the catch command is on cooldown for {1} seconds"
            self.CatchCooldown = 60.0
            self.CatchMaxAmount = 10
            self.CatchMaxAmountResponse = "{0} already has {1} Pokemon!"
            self.DuelCommand = "!duel"
            self.DuelResponse = "{0}'s {1} has challenged {2}'s {3} to a duel!"
            self.DuelPointsBasedOnLevel = True
            self.DuelPointsForWin = "1.5"
            self.DuelPointsForLoss = "0.5"
            self.DuelCooldownResponse = "{0} the duel command is on cooldown for {1} seconds"
            self.DuelCooldown = 60.0
            self.AcceptDuelCommand = "!acceptduel"
            self.AcceptDuelResponse = "{0} has accepted their duel with {1}"
            self.AcceptDuelOutcomeResponse = "{0} and their {2} absolutely demolished {1} and their {3}!"
            self.AcceptDuelMissingMonResponse = "{0} doesn't have a {1}"
            self.AcceptDuelNoDuelFoundResponse = "{0} and {1} doesn't have an duel pending"
            self.AcceptDuelOnCooldownResponse = "{0} the acceptduel command is on cooldown for {1} seconds"
            self.AcceptDuelCooldown = 60.0

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
    weapon = ""
    treasure = ""

# ---------------------------------------
# Functions used in commands
# -----------------------------------------------------------------------------------------------------------------------

def AddToFile(filepath, addme):
    with open(filepath, "a") as outfile:
        json.dump(addme, outfile, indent=4)
    #with open(filepath, "a+") as f:
        #f.seek(0)
        #data = f.read(100)
        #if len(data) > 0:
            #f.write("\n")
        #f.write(addme)

# -----------------------------------------------------------------------------------------------------------------------

def OverwriteNumberInFile(filepath, howmuchtoadd):
    if int(GetNumberFromFile(filepath)) != 0:
        newlevel = str(int(GetNumberFromFile(filepath)) + howmuchtoadd)
    else:
        newlevel = str(howmuchtoadd)
    with codecs.open(filepath, "a+", encoding="utf-8-sig") as f:
        f.seek(0)
        f.write(newlevel)

# -----------------------------------------------------------------------------------------------------------------------

def HasPermission(data):
    #Return true if user has permission and false if the user doesn't
    if not Parent.HasPermission(data.User, MySet.MonsterPermission, MySet.PermissionInfo):
        message = MySet.MonsterPermissionResp.format(data.UserName, MySet.MonsterPermission, MySet.PermissionInfo)
        SendResp(data, message)
        return False
    return True

# -----------------------------------------------------------------------------------------------------------------------

def GetUserPokemon(username):
    if os.path.exists(UsersMonFolder + username + ".txt"):
        response = ReadLinesFile(UsersMonFolder + username + ".txt")
    else:
        response = False
    return response

# -----------------------------------------------------------------------------------------------------------------------

def GetNumberFromFile(filepath):
    if os.path.exists(filepath):
        response = ReadLineFile(filepath)
    else:
        response = 0
    return response

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

def ExistsInFile(username, meexists):
    PokemonExists = False
    if GetUserPokemon(username):
        for line in GetUserPokemon(username):
            if line == meexists:
                PokemonExists = True
    return PokemonExists

# -----------------------------------------------------------------------------------------------------------------------

def RemoveFromFile(filepath, tmppath, removeme):
    a = ""
    with codecs.open(filepath, "r+", encoding="utf-8-sig") as fin:
        for line in fin:
            # only writes pokemon to the new file where it isn't the pokemon youve selected to release, case insensitive
            if removeme not in line.strip("\r\n"):
                a = a + line
        with codecs.open(tmppath, "w", encoding="utf-8-sig") as fout:
            fout.write(a)
    # am doing these extremely long windedly, likely a better way to remove blank lines
    with open(tmppath, 'r+') as fd:
        lines = fd.readlines()
        fd.seek(0)
        fd.writelines(line for line in lines if line.strip())
        fd.truncate()
    os.remove(filepath)
    os.rename(tmppath, filepath)

# -----------------------------------------------------------------------------------------------------------------------

def LiveCheck():
    if MySet.OnlyLive and not Parent.IsLive():
        return False
    else:
        return True

# -----------------------------------------------------------------------------------------------------------------------

def GetRandomLine(filepath):
    # i've had to get random line a really roundabout way, random.sample isnt picking up last line in file
    randnum = Parent.GetRandom(0, CountLines(filepath))
    lines_to_read = [
        randnum]  # this could be [0,1] and it'd return more than one line, if you did print lines or put into a list of something

    a_file = codecs.open(filepath, "r", encoding="utf-8-sig")
    for position, line in enumerate(a_file):
        if position in lines_to_read:
            return line

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

def GetTmpPath(filepath):
    tmp_filepath = str(filepath).replace(".txt","tmp.txt")
    return tmp_filepath

# needed to create this pokemon as it was hardcoding an initial value of test, so needed it to create this path at run time..
def GetLevelPath(username,Pokemon):
    return UsersMonLevelsFolder + username + "_" + Pokemon + ".txt"

def GetLevel(username,Pokemon):
    return GetNumberFromFile(GetLevelPath(username,Pokemon))

def GetUserPointsPath(UserStarted):
    return PointsFolder + UserStarted + ".txt"
    
def GetTargetPointsPath(TargetOf):
    return PointsFolder + TargetOf + ".txt"

# -----------------------------------------------------------------------------------------------------------------------

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

    global Pokemon
    global UserStarted
    global TargetOf
    global userpath
    global userencounterpath
    global encounterfile
    Pokemon = "test"
    UserStarted = "test"
    TargetOf = "test"
    userpath = UsersMonFolder + data.UserName + ".txt"
    userencounterpath = EncounterFolder + data.UserName + ".json"

    random.seed()

    # -----------------------------------------------------------------------------------------------------------------------
    #   Encounter
    # -----------------------------------------------------------------------------------------------------------------------

    if not data.IsWhisper() and data.IsChatMessage() and not data.IsFromDiscord() and data.GetParam(
            0).lower() == MySet.EncounterCommand.lower() and LiveCheck() and MySet.TurnOnEncounter:
        if not Parent.IsOnUserCooldown(ScriptName, MySet.EncounterCommand, data.User):
            # if the user doesn't have anything captured, then create an empty file
            #if not os.path.exists(userpath):
            #    create = open(userpath, "w+")
            if not os.path.exists(userpath):
                create = open(userpath, "w+")

            # if the user had a previous encounter, delete it
            #if os.path.exists(userencounterpath):
            #    os.remove(userencounterpath)

            # Adds the latest encounter to the encounter file
            #AddToFile(userencounterpath, RandomMonster)

            # gets a random line from the encounter files
            # This is the encounter which is selected
            encounters = ReadLinesFile(EncounterFile)
            #RandomEncounter = encounters[Parent.GetRandom(0, len(encounters))]

            EncounterList = []
            RandomEncounter = Encounter()

            with open(EncounterFile) as json_file:
                newEncounter = json.load(json_file)
                for e in newEncounter['encounters']:
                    en = Encounter()
                    en.encounter = e['encounter']
                    en.exp = e['exp']
                    en.weapon = e['weapon']
                    en.treasure = e['treasure']
                    EncounterList.append(en)

                randnum = Parent.GetRandom(0, len(EncounterList))
                RandomEncounter = EncounterList[randnum]

            data2 = ""

            #If this is the first time running the encounter script, make the user a new .json file
            if not os.path.exists(userencounterpath):
                create = open(userencounterpath, "w+")
                create.close()
                data2 = {}
                #Add the Experience from the encounter
                data2['exp'] = RandomEncounter.exp
                #Add the Weapons from the encounter
                data2['weapons'] = []
                if not RandomEncounter.weapon == "null":
                    data2['weapons'].append(RandomEncounter.weapon)
                #Add the Treasure from the encounter
                data2['treasure'] = []
                if not RandomEncounter.treasure == "null":
                    data2['treasure'].append(RandomEncounter.treasure)
            #If the user already has a .json file, open it and add the new data to it
            else:
                with open(userencounterpath) as json_file:
                    data2 = json.load(json_file)
                    #Add the Experience from the encounter
                    value = data2['exp'] + RandomEncounter.exp
                    data2['exp'] = value
                    #Add The Weapons from the encounter
                    if not RandomEncounter.weapon == "null":
                        data2['weapons'].append(RandomEncounter.weapon)
                    #Add the Treasure from the encounter
                    if not RandomEncounter.treasure == "null":
                        data2['treasure'].append(RandomEncounter.treasure)

            if os.path.exists(userencounterpath):
                os.remove(userencounterpath)

            AddToFile(userencounterpath, data2)

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

            formattedEncounter = RandomEncounter.encounter.replace('{0}', data.UserName)\
                .replace('{1}', GetRandomMonster())\
                .replace('{2}', GetRandomMonster())\
                .replace('{3}', str(GetRandomTime()))\
                .replace('{4}', GetRandomWeapon())\
                .replace('{5}', GetRandomSpell())\
                .replace('{6}', GetRandomTreasure())\
                .replace('{7}', GetRandomBodyPart())\
                .replace('{8}', GetRandomLocation())\
                .replace('{9}', GetRandomNPC())

            # constructs a response message based on parameters given in SL chatbot UI
            response = MySet.EncounterResponse.format(formattedEncounter)

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
    #   Catch
    # -----------------------------------------------------------------------------------------------------------------------
    if not data.IsWhisper() and data.IsChatMessage() and not data.IsFromDiscord() and data.GetParam(
            0).lower() == MySet.CatchCommand.lower() and LiveCheck() and MySet.TurnOnCatch:
        if not Parent.IsOnUserCooldown(ScriptName, MySet.CatchCommand, data.User):

            #- check to see how many mon users have, if more than allowed amount, stop and send response
            if CountLines(userpath) >= int(MySet.CatchMaxAmount):
                message = MySet.CatchMaxAmountResponse.format(data.UserName, MySet.CatchMaxAmount)
                Parent.SendStreamMessage(str(message))

            else:
                # vars -----------------------------------------------------------------------------------------------
                arg1 = data.GetParam(1)
                Pokemon = arg1.capitalize()
                # vars -----------------------------------------------------------------------------------------------

                if os.path.exists(userencounterpath):                                                           # if they've encountered a mon in !encounter
                    if Pokemon in ReadLinesFile(userencounterpath):                                             # and the !catch mon is in there
                        AddToFile(userpath, Pokemon)                                                            # add mon to their list
                        OverwriteNumberInFile(GetLevelPath(data.UserName,Pokemon), 1)                                                 # add mon level
                        os.remove(userencounterpath)                                                            # remove from encounter folder for this user
                        SendMessage(MySet.CatchResponse.format(data.UserName, "caught a", Pokemon))             # send success message
                        Parent.AddUserCooldown(ScriptName, MySet.CatchCommand, data.User, MySet.CatchCooldown)  # add cd
                    else:
                        SendMessage(MySet.CatchNotFoundResponse.format(data.UserName, Pokemon))
        else:
            cooldownduration = Parent.GetUserCooldownDuration(ScriptName, MySet.CatchCommand, data.User)
            message = MySet.CatchCooldownResponse.format(data.UserName, cooldownduration)
            Parent.SendStreamMessage(str(message))

    # -----------------------------------------------------------------------------------------------------------------------
    #   Battle
    # -----------------------------------------------------------------------------------------------------------------------
    if not data.IsWhisper() and data.IsChatMessage() and not data.IsFromDiscord() and data.GetParam(
            0).lower() == MySet.BattleCommand.lower() and LiveCheck() and MySet.TurnOnBattle:
        if not Parent.IsOnUserCooldown(ScriptName, MySet.BattleCommand, data.User):

            # if they've supplied a parameter, use that as the Mon, else get a random Mon from the list of users pokemon
            if len(data.GetParam(1)) > 0:
                reRandomUserPokemon = data.GetParam(1)
            else:
                reRandomUserPokemon = GetRandomLine(userpath)
            Pokemon = reRandomUserPokemon.capitalize().strip()

            # if supplied Mon parameter isn;t a pokemon they have, send error otherwise continue
            if ExistsInFile(data.UserName, Pokemon) == False:
                return Parent.SendStreamMessage("User does not have that Pokemon")
            else:
                # vars -----------------------------------------------------------------------------------------------
                # dont know why but this multiplier max seems to be 1.5 when i put 2.5
                Multiplier = random.uniform(0.5, 2.5)
                RandomMonster = random.choice(ReadLinesFile(MonsterFile))
                RandomPokemonLevel = int((int(GetLevel(data.UserName,Pokemon)) * Multiplier )) + 1
                deathflag = False
                
                # vars -----------------------------------------------------------------------------------------------

                # if user won, then use the won battle text file, and add a level if they aren't Max Level or above
                if int(MySet.BattleWinChance) >= Parent.GetRandom(1, 100):
                    RandomBattleResponse = random.choice(ReadLinesFile(FilePath + "wonbattle.txt"))
                    OverwriteNumberInFile(GetUserPointsPath(UserStarted), MySet.BattlePointsWin)
                    if int(GetLevel(data.UserName,Pokemon)) < MySet.BattleMaxLevel:
                        OverwriteNumberInFile(GetLevelPath(data.UserName,Pokemon), 1)

                # if they didn't win, they lost, if death chance procs, the use deathbattle response and activate death flag
                elif float(MySet.BattleDeathChance) >= float(Parent.GetRandom(1, 100)):
                    RandomBattleResponse = random.choice(ReadLinesFile(FilePath + "deathbattle.txt"))
                    OverwriteNumberInFile(GetUserPointsPath(UserStarted), - MySet.BattlePointsWin)
                    deathflag = True

                # if they didnt win, or activate death, then its just a loss, no levels gained
                else:
                    RandomBattleResponse = random.choice(ReadLinesFile(FilePath + "lostbattle.txt"))
                    OverwriteNumberInFile(GetUserPointsPath(UserStarted), - MySet.BattlePointsWin)

                # the random opponent level they will fight against, capped at BattleMaxLevel
                if int(RandomPokemonLevel) >= MySet.BattleMaxLevel:
                    RandomPokemonLevel = str(MySet.BattleMaxLevel)


                # generates the response text, based on whether they won or lost, and the params given in SL chatbot
                response = MySet.BattleResponse.format(data.UserName                        #{0}
                                                      , GetLevel(data.UserName,Pokemon)     #{1}
                                                      , Pokemon                             #{2}
                                                      , str(RandomPokemonLevel)             #{3}
                                                      , RandomMonster                       #{4}
                                                      , str(RandomBattleResponse).format(# the battle response text itself is #{5}, but can use the others
                                                                                         data.UserName                      #{0}
                                                                                       , GetLevel(data.UserName,Pokemon)    #{1}
                                                                                       , Pokemon                            #{2}
                                                                                       , str(RandomPokemonLevel)            #{3}
                                                                                       , RandomMonster)                     #{4}
                                                      )

                # if they proc'd the deathchance, remove that Mon from the userlist of Mon, and from the levels folder
                if deathflag:

                    RemoveFromFile(userpath, GetTmpPath(userpath), Pokemon)
                    os.remove(GetLevelPath(data.UserName,Pokemon))

            Parent.SendStreamMessage(str(response))
            Parent.AddUserCooldown(ScriptName, MySet.BattleCommand, data.User, MySet.BattleCooldown)

        else:
            cooldownduration = Parent.GetUserCooldownDuration(ScriptName, MySet.BattleCommand, data.User)
            message = MySet.BattleCooldownResponse.format(data.UserName, cooldownduration)
            Parent.SendStreamMessage(str(message))
    # -----------------------------------------------------------------------------------------------------------------------
    #   Release
    # -----------------------------------------------------------------------------------------------------------------------
    if not data.IsWhisper() and data.IsChatMessage() and not data.IsFromDiscord() and data.GetParam(
            0).lower() == MySet.ReleaseCommand.lower() and LiveCheck() and MySet.TurnOnRelease:
        if not Parent.IsOnUserCooldown(ScriptName, MySet.ReleaseCommand, data.User):
            # vars -----------------------------------------------------------------------------------------------

            rePokemon = data.GetParam(1)
            Pokemon = rePokemon.capitalize()
            UserMon = False

            # vars -----------------------------------------------------------------------------------------------

            # only if pokemon supplied exists does it do this, reads a, writes to b, deletes a, renames b to a
            if ExistsInFile(data.UserName, Pokemon):
                # remove from user file
                RemoveFromFile(userpath, GetTmpPath(userpath), Pokemon)
                # above fn doesnt remove the file, only removes pokemon
                os.remove(GetLevelPath(data.UserName,Pokemon))
                UserMon = True
            if UserMon:
                response = MySet.ReleaseResponse.format(data.User, Pokemon)
            else:
                response = MySet.ReleaseFailedResponse.format(data.User, Pokemon)
            SendMessage(response)
            Parent.AddUserCooldown(ScriptName, MySet.ReleaseCommand, data.User, MySet.ReleaseCooldown)
        else:
            cooldownduration = Parent.GetUserCooldownDuration(ScriptName, MySet.ReleaseCommand, data.User)
            message = MySet.ReleaseOnCooldownResponse.format(data.UserName, cooldownduration)
            SendMessage(str(message))
    # -----------------------------------------------------------------------------------------------------------------------
    #   Initiate Trade
    # -----------------------------------------------------------------------------------------------------------------------
    if not data.IsWhisper() and data.IsChatMessage() and not data.IsFromDiscord() and data.GetParam(
            0).lower() == MySet.TradeCommand.lower() and LiveCheck() and MySet.TurnOnTrade:
        if not Parent.IsOnUserCooldown(ScriptName, MySet.TradeCommand, data.User):
            # vars -----------------------------------------------------------------------------------------------
            TargetOf = str(data.GetParam(1)).strip("@")
            UserStarted = data.UserName

            # have to do two variables because capitalise doesnt seem to work properly otherwise
            a = data.GetParam(2)
            b = data.GetParam(3)
            UserPokemon = a.capitalize()
            TargetPokemon = b.capitalize()

            # vars -----------------------------------------------------------------------------------------------
            # checking an open trade doesnt already exist ( user a + user b are considered different trades than user b + user a)
            for filename in os.listdir(OpenTradesFolder):
                if UserStarted + "_" + TargetOf in filename:
                    SendMessage("you both already have an open trade, reject that one first")
                    return

            # these # below are to search through string and identify the pokemon without having to put in params
            TradePath = OpenTradesFolder + UserStarted + "_" + TargetOf + "#" + UserPokemon + "#" + TargetPokemon + "#.txt"
            # check whether user and target they actually have the pokemon, and then whether the trade already exists
            if not ExistsInFile(UserStarted, UserPokemon):
                SendMessage(UserStarted + " doesn't have a " + UserPokemon + " to trade!")
                return
            if not ExistsInFile(TargetOf, TargetPokemon):
                SendMessage(TargetOf + " doesn't have a " + TargetPokemon + " to trade!")
                return
            if os.path.exists(TradePath):
                SendMessage(UserStarted + ", that trade is already exists!, " + TargetOf + " needs to accept!")
                return

            # if doesnt exist, write any content but with the filename defined before.
            else:
                with codecs.open(TradePath, "a+", encoding="utf-8-sig") as f:
                    f.write("1")

            SendMessage(MySet.TradeResponse.format(UserStarted, TargetOf, UserPokemon, TargetPokemon))
            Parent.AddUserCooldown(ScriptName, MySet.TradeCommand, data.User, MySet.TradeCooldown)
        else:
            cooldownduration = Parent.GetUserCooldownDuration(ScriptName, MySet.TradeCommand, data.User)
            message = MySet.TradeOnCooldownResponse.format(data.UserName, cooldownduration)
            SendMessage(str(message))

    # -----------------------------------------------------------------------------------------------------------------------
    #   AcceptTrade
    # -----------------------------------------------------------------------------------------------------------------------
    if not data.IsWhisper() and data.IsChatMessage() and not data.IsFromDiscord() and data.GetParam(
            0).lower() == MySet.AcceptTradeCommand.lower() and LiveCheck() and MySet.TurnOnAcceptTrade:
        if not Parent.IsOnUserCooldown(ScriptName, MySet.AcceptTradeCommand, data.User):
            # vars -----------------------------------------------------------------------------------------------

            UserStarted = data.GetParam(1).strip("@")
            TargetOf = data.UserName
            hash1position = 0
            hash2position = 0
            hash3position = 0
            x = 0
            filefound = False
            UserStartedpath = UsersMonFolder + UserStarted + ".txt"
            Targetpath = UsersMonFolder + TargetOf + ".txt"

            # vars -----------------------------------------------------------------------------------------------

            # Extracting the Mon to trade and tradee from the filename
            for filename in os.listdir(OpenTradesFolder):
                if UserStarted + "_" + TargetOf in filename:
                    filefound = True
                    # loops through the text of filename, and works out what char indexes contain the hash, which is what in !trade
                    # we've set as the delimiters , files in format of user1_user2#Mon1#Mon2, so between from 1st #
                    # to 2nd # is Mon1, 2nd and 3rd # is Mon2
                    for i in range(len(filename)):
                        if filename.startswith("#", i):
                            x += 1
                            if x == 1:
                                hash1position = i
                            elif x == 2:
                                hash2position = i
                            elif x == 3:
                                hash3position = i
                    UserPokemon = filename[hash1position + 1:hash2position]
                    TargetPokemon = filename[hash2position + 1:hash3position]

                    # checks whether users and target still have the mon to trade, as could have removed after !trade was initiated
                    if GetNumberFromFile(UsersMonLevelsFolder + UserStarted + "_" + UserPokemon + ".txt") == False:
                        SendMessage(MySet.AcceptTradeMissingMonResponse.format(UserStarted, UserPokemon))
                        return
                    if GetNumberFromFile(UsersMonLevelsFolder + TargetOf + "_" + TargetPokemon + ".txt") == False:
                        SendMessage(MySet.AcceptTradeMissingMonResponse.format(TargetOf, TargetPokemon))
                        return

                    # Removes Pokemon from users
                    RemoveFromFile(UsersMonFolder + UserStarted + ".txt",
                                   UsersMonFolder + "tmp_" + UserStarted + ".txt", UserPokemon)
                    RemoveFromFile(UsersMonFolder + TargetOf + ".txt",
                                   UsersMonFolder + "tmp_" + TargetOf + ".txt", TargetPokemon)
                    # Adds new ones
                    AddToFile(UserStartedpath, TargetPokemon)
                    AddToFile(Targetpath, UserPokemon)
                    # swaps the files to swap pokemon levels as well
                    # right now this fails if you try to trade the same mon, (might want to due to levels)
                    os.rename(UsersMonLevelsFolder + UserStarted + "_" + UserPokemon + ".txt",
                              UsersMonLevelsFolder + TargetOf + "_" + UserPokemon + ".txt")
                    os.rename(UsersMonLevelsFolder + TargetOf + "_" + TargetPokemon + ".txt",
                              UsersMonLevelsFolder + UserStarted + "_" + TargetPokemon + ".txt")
                    # removes the trade from the list of trades
                    os.remove(OpenTradesFolder + filename)

            if filefound:
                completed_text = MySet.AcceptTradeResponse.format(TargetOf, UserStarted)
            else:
                completed_text = MySet.AcceptTradeNoTradeFoundResponse.format(UserStarted, TargetOf)

            SendMessage(completed_text)
            Parent.AddUserCooldown(ScriptName, MySet.AcceptTradeCommand, data.User, MySet.AcceptTradeCooldown)
        else:
            cooldownduration = Parent.GetUserCooldownDuration(ScriptName, MySet.AcceptTradeCommand, data.User)
            message = MySet.AcceptTradeOnCooldownResponse.format(data.UserName, cooldownduration)
            SendMessage(str(message))

    # -----------------------------------------------------------------------------------------------------------------------
    #   Refuse Trade
    # -----------------------------------------------------------------------------------------------------------------------
    if not data.IsWhisper() and data.IsChatMessage() and not data.IsFromDiscord() and data.GetParam(
            0).lower() == MySet.RefuseCommand.lower() and LiveCheck() and MySet.TurnOnRefuse:
        if not Parent.IsOnUserCooldown(ScriptName, MySet.RefuseCommand, data.User):
            # vars -----------------------------------------------------------------------------------------------

            UserStarted = data.GetParam(1).strip("@")
            TargetOf = data.UserName
            tradeexists = False

            # vars -----------------------------------------------------------------------------------------------
            # checks whether user1_user2 is contained in any filenames, it shouldnt have more than 1 open, as !trade command should have errored
            for filename in os.listdir(OpenTradesFolder):
                if UserStarted + "_" + TargetOf in filename:
                    file = filename
                    tradeexists = True

            if tradeexists:
                os.remove(OpenTradesFolder + file)
            else:
                SendMessage(MySet.RefuseNotFoundResponse.format(TargetOf, UserStarted))
                return

            SendMessage(MySet.RefuseResponse.format(TargetOf, UserStarted))
            Parent.AddUserCooldown(ScriptName, MySet.RefuseCommand, data.User, MySet.RefuseCooldown)
        else:
            cooldownduration = Parent.GetUserCooldownDuration(ScriptName, MySet.RefuseCommand, data.User)
            message = MySet.RefuseCooldownResponse.format(data.UserName, cooldownduration)
            SendMessage(str(message))
    # -----------------------------------------------------------------------------------------------------------------------
    #   Initiate Duel
    # -----------------------------------------------------------------------------------------------------------------------
    if not data.IsWhisper() and data.IsChatMessage() and not data.IsFromDiscord() and data.GetParam(
            0).lower() == MySet.DuelCommand.lower() and LiveCheck() and MySet.TurnOnDuel:
        if not Parent.IsOnUserCooldown(ScriptName, MySet.RefuseCommand, data.User):
            
            # vars -----------------------------------------------------------------------------------------------
            TargetOf = str(data.GetParam(1)).strip("@")
            UserStarted = data.UserName

            # have to do two variables because capitalise doesnt seem to work properly otherwise
            a = data.GetParam(2)
            b = data.GetParam(3)
            UserPokemon = a.capitalize()
            TargetPokemon = b.capitalize()

            # vars -----------------------------------------------------------------------------------------------
            # checking an open duel doesnt already exist ( user a + user b are considered different duel than user b + user a)
            for filename in os.listdir(OpenDuelsFolder):
                if UserStarted + "_" + TargetOf in filename:
                    SendMessage("you both already have an open duel, reject that one first")
                    return

            # these # below are to search through string and identify the pokemon without having to put in params
            DuelPath = OpenDuelsFolder + UserStarted + "_" + TargetOf + "#" + UserPokemon + "#" + TargetPokemon + "#.txt"
            # check whether user and target they actually have the pokemon, and then whether the duel already exists
            if not ExistsInFile(UserStarted, UserPokemon):
                SendMessage(UserStarted + " doesn't have a " + UserPokemon + " to duel with!")
                return
            if not ExistsInFile(TargetOf, TargetPokemon):
                SendMessage(TargetOf + " doesn't have a " + TargetPokemon + " to duel with!")
                return
            if os.path.exists(DuelPath):
                SendMessage(
                    UserStarted + ", that duel is already exists!, " + TargetOf + " needs to accept!")
                return

            # if doesnt exist, make new one, write any content but with the filename defined before.
            else:
                with codecs.open(DuelPath, "a+", encoding="utf-8-sig") as f:
                    f.write("1")

            SendMessage(
                MySet.DuelResponse.format(UserStarted, TargetOf, UserPokemon, TargetPokemon))
            Parent.AddUserCooldown(ScriptName, MySet.DuelCommand, data.User, MySet.DuelCooldown)
        else:
            cooldownduration = Parent.GetUserCooldownDuration(ScriptName, MySet.DuelCommand, data.User)
            message = MySet.DuelCooldownResponse.format(data.UserName, cooldownduration)
            SendMessage(str(message))

        # -----------------------------------------------------------------------------------------------------------------------
        #   Accept Duel
        # -----------------------------------------------------------------------------------------------------------------------
    if not data.IsWhisper() and data.IsChatMessage() and not data.IsFromDiscord() and data.GetParam(
            0).lower() == MySet.AcceptDuelCommand.lower() and LiveCheck() and MySet.TurnOnAcceptDuel:
        if not Parent.IsOnUserCooldown(ScriptName, MySet.AcceptDuelCommand, data.User):
            # vars -----------------------------------------------------------------------------------------------

            UserStarted = data.GetParam(1).strip("@")
            TargetOf = data.UserName
            hash1position = 0
            hash2position = 0
            hash3position = 0
            x = 0
            filefound = False
            # vars -----------------------------------------------------------------------------------------------

            # Extracting the Mon to duel and duele from the filename
            for filename in os.listdir(OpenDuelsFolder):
                if UserStarted + "_" + TargetOf in filename:
                    filefound = True
                    filefoundname = filename
                    # loops through the text of filename, and works out what char indexes contain the hash, which is what in !duel
                    # we've set as the delimiters , files in format of user1_user2#Mon1#Mon2, so between from 1st #
                    # to 2nd # is Mon1, 2nd and 3rd # is Mon2
                    for i in range(len(filename)):
                        if filename.startswith("#", i):
                            x += 1
                            if x == 1:
                                hash1position = i
                            elif x == 2:
                                hash2position = i
                            elif x == 3:
                                hash3position = i
                    UserPokemon = filename[hash1position + 1:hash2position]
                    TargetPokemon = filename[hash2position + 1:hash3position]

                    UserLevelStartedpath = UsersMonLevelsFolder + UserStarted + "_" + UserPokemon + ".txt"
                    TargetLevelpath = UsersMonLevelsFolder + TargetOf + "_" + TargetPokemon + ".txt"
                    UserPokemonLevel = int(GetNumberFromFile(UserLevelStartedpath))
                    TargetPokemonLevel = int(GetNumberFromFile(TargetLevelpath))


                    # checks whether users and target still have the mon to duel, as could have removed after !duel was initiated
                    if UserPokemonLevel == False:
                        SendMessage(MySet.AcceptDuelMissingMonResponse.format(UserStarted, UserPokemon))
                        return
                    if TargetPokemonLevel == False:
                        SendMessage(MySet.AcceptDuelMissingMonResponse.format(TargetOf, TargetPokemon))
                        return

                    WinChance = float(UserPokemonLevel)/ (float(UserPokemonLevel) + float(TargetPokemonLevel)) * 100

            if filefound:
                start_duel = MySet.AcceptDuelResponse.format(TargetOf, UserStarted)
                if WinChance >= Parent.GetRandom(1, 100):
                    winner = UserStarted
                    winnermon = UserPokemon
                    loser = TargetOf
                    losermon = TargetPokemon
                    if MySet.DuelPointsBasedOnLevel:
                        winnerpoints = int(TargetPokemonLevel * float(MySet.DuelPointsForWin))
                        loserpoints = - int(UserPokemonLevel * float(MySet.DuelPointsForLoss))
                    else:
                        winnerpoints = int(MySet.DuelPointsForWin)
                        loserpoints = -int(MySet.DuelPointsForLoss)
                    OverwriteNumberInFile(GetUserPointsPath(UserStarted), winnerpoints)
                    OverwriteNumberInFile(GetTargetPointsPath(TargetOf),  loserpoints)

                else:
                    winner = TargetOf
                    winnermon = TargetPokemon
                    loser = UserStarted
                    losermon = UserPokemon

                    if MySet.DuelPointsBasedOnLevel:
                        winnerpoints = int(UserPokemonLevel * float(MySet.DuelPointsForWin))
                        loserpoints = - int(TargetPokemonLevel * float(MySet.DuelPointsForLoss))
                    else:
                        winnerpoints = int(MySet.DuelPointsForWin)
                        loserpoints = int(-MySet.DuelPointsForLoss)

                    OverwriteNumberInFile(GetUserPointsPath(UserStarted), loserpoints)
                    OverwriteNumberInFile(GetTargetPointsPath(TargetOf), winnerpoints)

            else:
                SendMessage(MySet.AcceptDuelNoDuelFoundResponse.format(UserStarted, TargetOf))
                return

            dueloutcome = MySet.AcceptDuelOutcomeResponse.format(winner,loser,winnermon,losermon)
            os.remove(OpenDuelsFolder + filefoundname)
            SendMessage(start_duel)
            SendMessage(dueloutcome)
            Parent.AddUserCooldown(ScriptName, MySet.AcceptDuelCommand, data.User, MySet.AcceptDuelCooldown)
        else:
            cooldownduration = Parent.GetUserCooldownDuration(ScriptName, MySet.AcceptDuelCommand, data.User)
            message = MySet.AcceptDuelOnCooldownResponse.format(data.UserName, cooldownduration)
            SendMessage(str(message))

    return


# ---------------------------
#   [Required] Tick method (Gets called during every iteration even when there is no incoming data)
# ---------------------------
def Tick():
    return


# ---------------------------
#   [Optional] Parse method (Allows you to create your own custom $parameters) 
# ---------------------------

def Parse(parseString, userid, username, targetid, targetname, message):
    # Gets all of the Users Pokemon

    if "$mypokemon" in parseString:
        if GetUserPokemon(username) != False:
            # need to str here because it breaks otherwise, other dependencies on fn cant let me string it there
            parseString = parseString.replace("$mypokemon", str(GetUserPokemon(username)))
        else:
            parseString = username + " has no pokemon"

    # releaseallpokemon parameter
    if "$releaseallpokemon" in parseString:
        if GetUserPokemon(username) == False:
            return username + " has no pokemon"
        for line in GetUserPokemon(username):
            os.remove(UsersMonLevelsFolder + username + "_" + line + ".txt")
        os.remove(userpath)

        parseString = parseString.replace("$releaseallpokemon", username + " has released all their pokemon")

    # Retrieves the level of the pokemon
    if "$pokemonlvl" in parseString:
        regexp = re.compile("\$pokemonlvl (\w+)")
        Pokemon = regexp.search(parseString).group(1)
        if GetNumberFromFile(GetLevelPath(username,Pokemon)) != 0:
            parseString = parseString.replace(regexp.search(parseString).group(0), GetNumberFromFile(GetLevelPath(username,Pokemon)))
        else:
            parseString = username + " does not have a " + Pokemon

    if "$numberofpokemon" in parseString:
        parseString = username + " has " + str(CountLines(UsersMonFolder + username + ".txt")) + " Pokemon"

    return parseString
