class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    def __str__(self):
        return f"이름: {self.name}"


player_dict = {
    13: Player("허경민", "내야수"),
    20: Player("안승한", "포수"),
    22: Player("장승현", "포수"),
    25: Player("양의지", "포수"),
    26: Player("박유연", "포수"),
    96: Player("윤준호", "포수"),
    3: Player("안갈비", "내야수"),
    5: Player("신성현", "내야수"),
    7: Player("이유찬", "내야수"),
    14: Player("박계범", "내야수"),
    16: Player("서예일", "내야수"),
    18: Player("김민혁", "내야수"),
    23: Player("강승호", "내야수"),
    34: Player("권민석", "내야수"),
    35: Player("전민재", "내야수"),
    52: Player("김재호", "내야수"),
    53: Player("양석환", "내야수"),
    93: Player("임서준", "내야수"),
    8: Player("송승환", "외야수"),
    11: Player("로하스", "외야수"),
    31: Player("정수빈", "외야수"),
    32: Player("김재환", "외야수"),
    37: Player("김대한", "외야수"),
    39: Player("김인태", "외야수"),
    44: Player("홍성호", "외야수"),
    49: Player("강진성", "외야수"),
    51: Player("조수행", "외야수"),
    57: Player("양찬열", "외야수")
}

players = []


def pick_player():
    while len(players) < 9:
        key_or_name = input(f"{len(players)+1}번 선수는 누구로 하시겠습니까? ")
        if key_or_name.isdigit():
            key = int(key_or_name)
            if key in player_dict:
                player = player_dict[key]
                if player.position == "내야수":
                    if players.count(player) >= 5:
                        print("내야수는 5명까지 선택할 수 있습니다. 다시 선택하세요.")
                        continue
                elif player.position == "외야수":
                    if players.count(player) >= 3:
                        print("외야수는 3명까지 선택할 수 있습니다. 다시 선택하세요.")
                        continue
                players.append(player)
                exec(f"player{len(players)} = player")
                print(f"{player.position} {player.name} 선수가 추가되었습니다.")

            else:
                print("잘못된 선택입니다. 다시 선택하세요.")

        else:
            name = key_or_name
            found_players = [player for player in player_dict.values() if player.name == name]
            if len(found_players) == 0:
                print("선택한 선수가 없습니다. 다시 선택하세요.")
                continue

            player = found_players[0]
            if player.position == "내야수":
                if players.count(player) >= 5:
                    print("내야수는 5명까지 선택할 수 있습니다. 다시 선택하세요.")
                    continue
            elif player.position == "외야수":
                if players.count(player) >= 3:
                    print("외야수는 3명까지 선택할 수 있습니다. 다시 선택하세요.")
                    continue
            players.append(player)
            exec(f"player{len(players)} = player")
            print(f"{player.position} {player.name} 선수가 추가되었습니다.")
    

def printing_players() :
    print("선수 정보:")
    for i, player in enumerate(players, start=1):
        exec(f"player{i} = player")
        print(f"{i}번 선수:")
        print(f"이름: {player.name}")
        print(f"포지션: {player.position}")
        print()



pick_player()
printing_players()
print(f"선택된 선수 수: {len(players)}명")
print(players)


