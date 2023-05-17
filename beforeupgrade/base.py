from batters_position import *
from beforeupgrade.findnameornumorposition import *
import random
from pickplayer import player
from pickplayer import Player
from pickplayer import players


inning = 1
play_again = "yes"

while play_again.lower() == "yes":
    print(f"{inning}회 시작!")
    base1 = None
    base2 = None
    base3 = None
    home = None
    doosan = 0

    strike_counts = {}
    foul_counts = {}

    for player in players:
        strike_counts[player] = 0
        foul_counts[player] = 0

    while True:  # 선수가 아웃되지 않은 한 무한루프
        current_player = random.choice(players)
        result = random.choice(["스트라이크", "헛스윙", "안타", "번트", "홈런"])
        print(f"{current_player.name}가 {result} 했습니다.")

        if result == "스트라이크" or result == "헛스윙":
            strike_counts[current_player] += 1
            foul_counts[current_player] += 1
            print(f"{current_player.name}가 {result} 했습니다.")
            print(f"{current_player.name}의 스트라이크 카운트가 {strike_counts[current_player]}이고, 파울 카운트가 {foul_counts[current_player]}입니다.")

            if strike_counts[current_player] == 3:
                print(f"{current_player.name} - 아웃되었습니다.")
                players.remove(current_player)
                 
                break  # 아웃된 선수이므로 루프 탈출

        elif result == "안타":
            hit_result = random.choice(["아웃", "플라이아웃", "1루타", "2루타", "3루타"])
            print(f"{current_player.name}가 {hit_result} 했습니다.")

            if hit_result == "1루타":
                if base1 is not None:
                    base2 = base1
                base1 = current_player
                print(f"{current_player.name}가 1루타 했습니다.")

            elif hit_result == "2루타":
                if base1 is not None:
                    base3 = base1
                    base1 = None
                if base2 is not None:
                    base3 = base2
                    base2 = None
                base2 = current_player
                print(f"{current_player.name}가 2루타 했습니다.")

            elif hit_result == "3루타":
                if base1 is not None:
                    home = base1
                    base1 = None
                if base2 is not None:
                    home = base2
                    base2 = None
                if base3 is not None:
                    home = base3
                    base3 = None
                base3 = current_player
                doosan += 1
                print(f"{current_player.name}가 3루타 했습니다.")

            else:
                print(f"{current_player.name} - {hit_result}!")
                players.remove(current_player)

            print("Bases:")
            print(f"1루: {base1}")
            print(f"2루: {base2}")
            print(f"3루: {base3}")
            print(f"홈: {home}")
            print(f"두산: {doosan}")
            print()

        elif result == "번트":
            print(f"{current_player.name} - 번트 성공!")
            if base1 is not None:
                base2 = base1
            base1 = current_player

            print("Bases:")
            print(f"1루: {base1}")
            print(f"2루: {base2}")
            print(f"3루: {base3}")
            print(f"홈: {home}")
            print()

        elif result == "홈런":
            print(f"{current_player.name} - 홈런!")
            if base1 is not None:
                doosan += 1
                players.remove(base1)
                base1 = None
                print("1루수에 있던 선수가 홈으로 들어갔습니다.")
                print("두산에 한 점! 총", doosan, "점!")
            if base2 is not None:
                doosan += 1
                players.remove(base2)
                base2 = None
                print("2루수에 있던 선수가 홈으로 들어갔습니다.")
                print("두산에 한 점! 총", doosan, "점!")
            if base3 is not None:
                doosan += 1
                players.remove(base3)
                base3 = None
                print("3루수에 있던 선수가 홈으로 들어갔습니다.")
                print("두산에 한 점! 총", doosan, "점!")
            doosan += 1
            print("현재 두산 점수:", doosan)
            players.remove(current_player)
            break  # 홈런 처리가 끝났으므로 루프 탈출

        print("Bases:")
        print(f"1루: {base1}")
        print(f"2루: {base2}")
        print(f"3루: {base3}")
        print(f"홈: {home}")
        print(f"두산: {doosan}")
        print()

    print("한 회!")
    print("Bases after the inning:")
    print(f"1루: {base1}")
    print(f"2루: {base2}")
    print(f"3루: {base3}")
    print(f"홈: {home}")
    print()
    print(f"두산: {doosan}")
    print()

    inning += 1

    play_again = input("다음 회를 시작할까요? (yes/no): ")
    print()

print("게임 종료!")
