from batters_position import *
from beforeupgrade.findnameornum import *

def search_by_value(players, value):
    result = []
    for key, player in players.items():
        if player.name == value or player.position == value:
            result.append((key, player))
    return result

def search_by_key(players, key):
    if key in players:
        return [(key, players[key])]
    else:
        return []

def search_by_key_value(players, value):
    result = []
    for key, player in players.items():
        if key == value or player.name == value or player.position == value:
            result.append((key, player))
            break
    return result