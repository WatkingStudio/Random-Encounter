﻿var settings = {
  "OnlyLive": false,
  "TurnOnEncounter": true,
  "TurnOnMonster": true,
  "TurnOnCheckLevel": true,
  "TurnOnCheckTreasure": true,
  "TurnOnEquipment": true,
  "TurnOnCheckLoot": true,
  "TurnOnCheckTrophies": true,
  "TurnOnEquip": true,
  "TurnOnQuest": true,
  "TurnOnJoin": true,
  "TurnOnRebalance": true,
  "TurnOnCatch": false,
  "TurnOnBattle": false,
  "TurnOnRelease": false,
  "TurnOnTrade": false,
  "TurnOnAcceptTrade": false,
  "TurnOnRefuse": false,
  "TurnOnDuel": false,
  "PointsName": "Street Rep",
  "InvalidDataResponse": "{0} does not have a valid data file",
  "GiveLootResponse": "{0} has been rewarded with a {1}",
  "EncounterCommand": "!test",
  "EncounterResponse": "{0}",
  "EncounterCooldownResponse": "{0} encounter command is on cooldown for {1} seconds !",
  "EncounterNumber": 1,
  "EncounterCooldown": 1.0,
  "MonsterCommand": "!addmonster",
  "MonsterPermission": "Moderator",
  "MonsterPermissionInfo": "Moderator",
  "MonsterPermissionResp": "$user -> only $permission ($permissioninfo) and higher can use this command",
  "MonsterResponse": "/me Added {0} to the monster script",
  "MonsterCooldownResponse": "{0}; the monster command is on cooldown for {1} seconds",
  "MonsterCooldown": 1.0,
  "CheckLevelCommand": "!level",
  "CheckLevelResponse": "{0} level is: {1}",
  "CheckLevelCooldownResponse": "{0} the level command is on cooldown for {1} seconds",
  "CheckLevelCooldown": 60.0,
  "CheckTreasureCommand": "!treasure",
  "CheckTreasureResponse": "{0} has {1} piles of treasure!",
  "CheckTreasureCooldownResponse": "{0} the treasure command is on cooldown for {1} seconds",
  "CheckTreasureCooldown": 60.0,
  "EquipmentCommand": "!equipment",
  "EquipmentWhisperResponse": "{0} check your twitch inbox for your equipment info, you may need to refresh.",
  "EquipmentMessage": "{0} has the following equipped: (head) {1}, (body) {2}, (hands) {3}, (legs) {4}, (feet) {5}, (right hand) {6}, (left hand) {7}, (back) {8}",
  "EquipmentSpecificResponse": "{0} has a {1} equipped on their {2}",
  "EquipmentCooldownResponse": "{0} the equipment command is on cooldown for {1} seconds",
  "EquipmentWhisperCooldown": 60.0,
  "EquipmentChatCooldown": 300.0,
  "CheckLootCommand": "!loot",
  "CheckLootWhisperResponse": "{0} check your twitch inbox for your loot info, you may need to refresh.",
  "CheckLootMessage": "{0} has the following loot: {1}",
  "CheckLootCooldownResponse": "{0} the loot command is on cooldown for {1} seconds",
  "CheckLootWhisperCooldown": 60.0,
  "CheckLootChatCooldown": 300.0,
  "CheckTrophiesCommand": "!trophies",
  "CheckTrophiesWhisperResponse": "{0} check your twitch inbox for your trophies info, you may need to refresh.",
  "CheckTrophiesMessage": "{0} has the following trophies: {1}",
  "CheckTrophiesCooldownResponse": "{0} the trophies command is on coodown for {1} seconds",
  "CheckTrophiesWhisperCooldown": 60.0,
  "CheckTrophiesChatCooldown": 300.0,
  "EquipCommand": "!equip",
  "EquipResponseSuccess": "{0} has successfully been equipped",
  "EquipResponseItemInvalid": "The item {0} is not a valid item",
  "EquipResponseLocationInvalid": "The location {0} is not a valid location for a {1}",
  "EquipResponseItemNotOwned": "You do not currently own the item '{0}' so you are not able to equip it",
  "EquipCooldownResponse": "{0} the equip command is on cooldown for {1} seconds",
  "EquipCooldown": 5.0,
  "QuestCommand": "!quest",
  "QuestResponse": "A quest has been started to hunt down a {0}. Type '!join' in the chat to join the quest.",
  "QuestActiveMessage": "There is currently an active quest with {0} seconds left to join the questing party",
  "QuestCountdownMessage": "You have {0} seconds to join the questing party",
  "QuestCountdown": 20.0,
  "QuestPermission": "Moderator",
  "QuestPermissionInfo": "Moderator",
  "QuestPermissionResponse": "{0} -> only $permission ({1}) and higher can use this command",
  "QuestInvalidMonsterResponse": "Invalid Monster Named, Selecting Random Monster",
  "QuestSuccessResponse": "The quest to slay the {0} has been successful. The questing party returns victorious!",
  "QuestFailedResponse": "The quest to slay the {0} has failed. The questing party managed to escape with their lives but return defeated.",
  "QuestCancelResponse": "The current quest has been cancelled.",
  "QuestErrorResponse": "There has been an error with this quest, please check the log files.",
  "JoinCommand": "!join",
  "JoinResponseSuccess": "{0} has joined the questing party",
  "JoinResponseNoQuest": "{0} this is currently no active quest",
  "JoinResponseFailed": "{0} is already a member of the questing party.",
  "JoinCooldownResponse": "{0} the join command is currently on cooldown for {1} seconds",
  "JoinCooldown": 1.0,
  "RebalanceCommand": "!rebalance",
  "RebalanceResponse": "Rebalancing Complete",
  "RebalancePermission": "Moderator",
  "RebalancePermissionInfo": "Moderator",
  "RebalancePermissionResp": "{0} -> only $permission ({1}) and higher can use this command",
  "BattleCommand": "!battle",
  "BattleResponse": "/me {5}",
  "BattleCooldownResponse": "/me {0}, the battle command is on cooldown for {1} seconds",
  "BattleWinChance": 75.0,
  "BattleDeathChance": "0",
  "BattlePointsWin": 10,
  "BattlePointsLoss": 10,
  "BattleMaxLevel": 100,
  "BattleCooldown": 1.0,
  "ReleaseCommand": "!release",
  "ReleaseResponse": "/me {0} has released their {1}",
  "ReleaseFailedResponse": "/me {0} does not have a {1}",
  "ReleaseOnCooldownResponse": "/me {0}, the release command is on cooldown for {1} seconds",
  "ReleaseCooldown": 1.0,
  "TradeCommand": "!trade",
  "TradeResponse": "/me {0} would like to trade their {2} for {1}'s {3}!",
  "TradeUserNotThatMonResponse": "/me {0} does not have a ",
  "TradeOnCooldownResponse": "/me {0}, the trade command is on cooldown for {1} seconds",
  "TradeCooldown": 60.0,
  "AcceptTradeCommand": "!AcceptTrade",
  "AcceptTradeResponse": "/me {0} has Accepted their trade with {1}",
  "AcceptTradeMissingMonResponse": "/me {0} doesn't have a {1}",
  "AcceptTradeNoTradeFoundResponse": "/me {0} and {1} don't have an trade pending",
  "AcceptTradeOnCooldownResponse": "/me {0} the AcceptTrade command is on cooldown for {1} seconds",
  "AcceptTradeCooldown": 60.0,
  "RefuseCommand": "!refuse",
  "RefuseResponse": "/me {0} refused to trade with {1}",
  "RefuseNotFoundResponse": "/me {0} and {1} don't have an trade pending",
  "RefuseCooldownResponse": "/me {0} the refuse command is on cooldown for {1} seconds",
  "RefuseCooldown": 60.0,
  "CatchCommand": "!catch",
  "CatchResponse": "/me {0} {1} {2}",
  "CatchNotFoundResponse": "/me {0} didnt encounter a {1}",
  "CatchCooldownResponse": "/me {0} the catch command is on cooldown for {1} seconds",
  "CatchCooldown": 1.0,
  "CatchMaxAmount": "10",
  "CatchMaxAmountResponse": "/me {0} already has {1} Pokemon!",
  "DuelCommand": "!duel",
  "DuelResponse": "/me {0}'s {2} has challenged {1}'s {3} to a duel!",
  "DuelPointsBasedOnLevel": true,
  "DuelPointsForWin": "1.5",
  "DuelPointsForLoss": "0.5",
  "DuelCooldownResponse": "{0} the duel command is on cooldown for {1} seconds",
  "DuelCooldown": 60.0,
  "AcceptDuelCommand": "!acceptduel",
  "AcceptDuelResponse": "/me {0} has accepted their duel with {1}",
  "AcceptDuelMissingMonResponse": "/me {0} doesn't have a {1}",
  "AcceptDuelNoDuelFoundResponse": "/me {0} and {1} don't have a duel pending",
  "AcceptDuelOnCooldownResponse": "/me {0} the AcceptDuel command is on cooldown for {1} seconds",
  "AcceptDuelCooldown": 1.0,
  "TurnOnAcceptDuel": false,
  "AcceptDuelOutcomeResponse": "/me {0} and their {2} absolutely demolished {1} and their {3}!"
};