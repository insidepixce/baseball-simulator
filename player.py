class Player:
    def __init__(self, name, position, number):
        self.name = name
        self.position = position
        self.number = number

    def __str__(self):
        return f"이름: {self.name}, 포지션: {self.position}"
