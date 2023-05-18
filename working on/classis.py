class Player:
    def __init__(self, name, position, number):
        self.name = name
        self.position = position
        self.number = number
        self.selected = False
player_dict = {
    13: Player("허경민", "내야수", 13),
    20: Player("안승한", "포수", 20),
    22: Player("장승현", "포수", 22),
    25: Player("양의지", "포수", 25),
    26: Player("박유연", "포수", 26),
    96: Player("윤준호", "포수", 96),
    3: Player("안갈비", "내야수", 3),
    5: Player("신성현", "내야수", 5),
    7: Player("이유찬", "내야수", 7),
    14: Player("박계범", "내야수", 14),
    16: Player("서예일", "내야수", 16),
    18: Player("김민혁", "내야수", 18),
    23: Player("강승호", "내야수", 23),
    34: Player("권민석", "내야수", 34),
    35: Player("전민재", "내야수", 35),
    52: Player("김재호", "내야수", 52),
    53: Player("양석환", "내야수", 53),
    93: Player("임서준", "내야수", 93),
    8: Player("송승환", "외야수", 8),
    11: Player("로하스", "외야수", 11),
    31: Player("정수빈", "외야수", 31),
    32: Player("김재환", "외야수", 32),
    37: Player("김대한", "외야수", 37),
    39: Player("김인태", "외야수", 39),
    44: Player("홍성호", "외야수", 44),
    49: Player("강진성", "외야수", 49),
    51: Player("조수행", "외야수", 51),
    57: Player("양찬열", "외야수", 57)
}

for player in player_dict.values():
    player.selected = False
    
    def __str__(self):
        return f"이름: {self.name}, 포지션: {self.position}, 번호: {self.number}"
