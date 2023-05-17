import random
from batters_position import *
from batters import *


# 선수들의 순서를 리스트로 저장
#
# 각 선수들의 변수값
strike_counts = {player: 0 for player in players}
foul_counts = {player: 0 for player in players}

# 베이스 초기화
base1 = None
base2 = None
base3 = None
home = None

# 두산 초기화
doosan = 0

# 이닝 시뮬레이션
for _ in range(1, 10):
    # 각 타자에게 랜덤한 결과 배정
    current_player = random.choice(players)
    result = random.choice(["스트라이크", "헛스윙", "안타", "번트", "홈런"])
    print(current_player,"가",result,"했습니다")

    # 스트라이크 또는 헛스윙인 경우
    if result == "스트라이크" or result == "파울":
        strike_counts[current_player] += 1
        foul_counts[current_player] += 1
        print(current_player,"의 스트라이크 카운트가",strike_counts,"이고, 파울 카운트가", foul_counts,"입니다")

        # 스트라이크와 헛스윙이 3회인 경우 아웃
        if strike_counts[current_player] == 3 and foul_counts[current_player] == 3:
            print(f"{current_player} - 가 아웃되었습니다")
            players.remove(current_player)

    # 안타인 경우
    elif result == "안타":
        hit_result = random.choice(["아웃", "플라이아웃", "1루타", "2루타", "3루타"])

        # 1루타인 경우
        if hit_result == "1루타":
            if base1 is not None:
                base2 = base1
            base1 = current_player

        # 2루타인 경우
        elif hit_result == "2루타":
            if base1 is not None:
                base3 = base1
                base1 = None
            if base2 is not None:
                base3 = base2
                base2 = None
            base2 = current_player

        # 3루타인 경우
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

        # 아웃인 경우
        else:
            print(f"{current_player} - {hit_result}!")
            players.remove(current_player)
        # 홈런인 경우
    elif result == "Home Run":
        if base1 is not None:
            doosan += 1
            players.remove(base1)
            base1 = None
            print("1루수에 있던 선수가 홈으로 들어갔습니다")
            print("두산에 한 점 !")
        if base2 is not None:
            doosan += 1
            players.remove(base2)
            base2 = None
            print("2루수에 있던 선수가 홈으로 들어갔습니다")
            print("두산에 한 점 !")
        if base3 is not None:
            doosan += 1
            players.remove(base3)
            base3 = None
            print("3루수에 있던 선수가 홈으로 들어갔습니다")
            print("두산에 한 점 !")
        doosan += 1
        players.remove(current_player)

# 이닝이 종료된 후 베이스 상황 출력
print("Bases after the inning:")
print(f"1루: {base1}")
print(f"2루: {base2}")
print(f"3루: {base3}")
print(f"홈: {home}")
print()

# 두산 점수 출력
print(f"두산: {doosan}")

            
