from batters_position import *
from findnameornumorposition import *

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
selected_players = set()  # 입력된 선수들을 저장할 집합(set)

for i in range(1, 10):
    while True:
        number = input(f"{i}번 선수는 누구로 하시겠습니까? (선수 번호 또는 이름 입력): ")

        # 입력된 번호 또는 이름으로 선수 찾기
        found_players = [player for player in player_dict.values() if player.number == number or player.name == number]

        if len(found_players) == 0:
            print("선택한 선수가 없습니다. 다시 선택하세요.")
        elif len(found_players) > 1:
            print("중복된 선수가 있습니다. 다시 선택하세요.")
        else:
            player = found_players[0]
            break

    if player in selected_players:
        print("이미 선택한 선수입니다. 다른 선수를 선택하세요.")
        continue

    if player.position == "내야수":
        if players.count(player) >= 5:
            print("내야수는 5명까지 선택할 수 있습니다. 다시 선택하세요.")
            continue
    elif player.position == "외야수":
        if players.count(player) >= 3:
            print("외야수는 3명까지 선택할 수 있습니다. 다시 선택하세요.")
            continue

    players.append(player)
    selected_players.add(player)

    print(f"{player.position} {player.name} 선수가 추가되었습니다.")

    # 현재까지 선택된 선수들의 목록 출력
    print("현재까지 선택된 선수들:")
    for selected_player in players:
        print(selected_player)

    print()

print(f"선택된 선수 수: {len(players)}명")

# 선택된 선수들의 정보 출력
print("선택된 선수들:")
for player in players:
    print(player)
