from batters_position import *
from beforeupgrade.findnameornumorposition import *


class Player:
    def __init__(self, name, position, number):
        self.name = name
        self.position = position
        self.number = number

    def __str__(self):
        return f"이름: {self.name}, 포지션: {self.position}"

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

players = []
selected_players = set()

while len(selected_players) < 9:
    number = input("선수를 입력하세요 (선수 번호 또는 이름): ")

    found_players = [player for player in player_dict.values() if player.number == number or player.name == number]

    if len(found_players) == 0:
        print("선택한 선수가 없습니다. 다시 선택하세요.")
    elif len(found_players) > 1:
        print("중복된 선수가 있습니다. 다시 선택하세요.")
    else:
        player = found_players[0]
        if player in selected_players:
            print("이미 선택한 선수입니다. 다른 선수를 선택하세요.")
        else:
            players.append(player)
            selected_players.add(player)
            print(f"{player.position} {player.name} 선수가 추가되었습니다.")

print("선수 선택이 완료되었습니다.")
print()

import pickle

# 선수들을 파일에 저장
with open('selected_players.pkl', 'wb') as file:
    pickle.dump(players, file)

