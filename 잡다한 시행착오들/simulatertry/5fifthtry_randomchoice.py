import random
from classis import Player
import pickle

# 저장된 선수들을 파일에서 불러오기
with open('selected_players.pkl', 'rb') as file:
    saved_players = pickle.load(file)

# 선수들을 리스트로 변환
players = list(saved_players)

# 선수들의 스트라이크, 헛스윙, 파울 카운트 초기화
strike_counts = {player: 0 for player in players}
foul_counts = {player: 0 for player in players}

# 베이스 초기화
base1 = None
base2 = None
base3 = None
home = None

# 두산 초기화
doosan = 0

print("경기를 시작합니다 ----------------))))")

while len(players) > 0:
    # 현재 타자 선택
    current_player = random.choice(players)
    print(f"{current_player.name}가 타석에 들어섰습니다.")

    # 스트라이크, 헛스윙 처리
    while strike_counts[current_player] < 3:
        result = random.choice(["스트라이크", "헛스윙", "치다", "홈런"])
        print(f"{current_player.name}가 {result} 했습니다.")

        if result == "스트라이크" or result == "헛스윙":
            strike_counts[current_player] += 1
            foul_counts[current_player] += 1
            print("스트라이크", strike_counts[current_player])
            print('파울', foul_counts[current_player])
            print('다음공 -----------------')

            if strike_counts[current_player] >= 3 or foul_counts[current_player] >= 4:
                if current_player in players:
                    players.remove(current_player)
                print(f"{current_player.name} - 아웃되었습니다.")
                print('다음타자 등장 -----------------')
                break

        # 안타인 경우
        elif result == "치다":
            hit_result = random.choice(["아웃", "플라이아웃", "1루타", "2루타", "3루타"])
            print(f"{current_player.name}가 {hit_result} 했습니다.")
            print("스트라이크", strike_counts[current_player])
            print('파울', foul_counts[current_player])
            print('다음공 -----------------')

            if hit_result == "1루타":
                if base1 is not None:
                    base2 = base1
                base1 = current_player

            elif hit_result == "2루타":
                if base1 is not None:
                    base3 = base1
                    base1 = None
                if base2 is not None:
                    base3 = base2
                    base2 = None
                base2 = current_player

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

            else:  # 아웃인 경우
                print(f"{current_player.name} - {hit_result}!")
                if current_player in players:
                    players.remove(current_player)
                print('다음타자 등장 ->-<->-<-------------')
                break

        # 홈런인 경우
        elif result == "홈런":
            if base1 is not None and base1 in players:
                doosan += 1
                players.remove(base1)
                base1 = None
                print("선수가 홈으로 들어갔습니다.")
                print("두산에 한 점!")
            if base2 is not None and base2 in players:
                doosan += 1
                players.remove(base2)
                base2 = None
                print("2루수에 있던 선수가 홈으로 들어갔습니다.")
                print("두산에 한 점!")
            if base3 is not None and base3 in players:
                doosan += 1
                players.remove(base3)
                base3 = None
                print("3루수에 있던 선수가 홈으로 들어갔습니다.")
                print("두산에 한 점!")
            if current_player in players:
                players.remove(current_player)
                print(f"{current_player.name} - 홈런!")
                doosan += 1

        # 베이스 상황 출력
        print("Bases after the play:")
        print(f"1루: {base1}")
        print(f"2루: {base2}")
        print(f"3루: {base3}")
        print(f"홈: {home}")
        print()

    # 이닝이 종료된 후 베이스 상황 출력
    print("Bases after the inning:")
    print(f"1루: {base1}")
    print(f"2루: {base2}")
    print(f"3루: {base3}")
    print(f"홈: {home}")
    print()

    # 두산 점수 출력
    print(f"두산: {doosan}")

print("경기 종료!")
