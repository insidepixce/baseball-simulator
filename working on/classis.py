from typing import List, Dict, Union

class Player:
    name: str
    position: str
    number: int
    selected: bool
    
    def __init__(self, name: str, position: str, number: str, selected: bool = False):
        self.name = name
        self.position = position
        self.number = number
        self.selected = selected

    def __str__(self):
        return f"이름: {self.name}, 포지션: {self.position}, 번호: {self.number}"

PlayerDict = Dict[str, Union[str, int, bool]]
PlayerList = List[Player] 

class Players:
    @staticmethod
    def to_list(players: PlayerList) -> List[PlayerDict]:
        return list(map(lambda player: player.__dict__, players))
    
    @staticmethod
    def to_players(players: List[PlayerDict]) -> PlayerList:
        return list(map(lambda player: Player(**player), players))