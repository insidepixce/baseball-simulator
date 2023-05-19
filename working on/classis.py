from typing import List, Dict, Union

class Player:
    name: str
    position: str
    number: int
    selected: bool
    

    def __init__(self, name, position, number, selected):

        self.name = name
        self.position = position
        self.number = number
        self.selected = selected



    def __str__(self):
        return f"이름: {self.name}, 포지션: {self.position}, 번호: {self.number}"
    
    def to_dict(self):
        return {
            'name': self.name,
            'position': self.position,
            'number': self.number,
            'selected': self.selected
        }

