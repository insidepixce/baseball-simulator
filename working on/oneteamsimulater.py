import random
import pickle

from classis import Player


# 이닝 후 베이스 상황 출력하는 함수
def basecall():
    print("이닝 종료 후 베이스 상황:")
    print(f"1루: {base1}")
    print(f"2루: {base2}")
    print(f"3루: {base3}")
    print(f"홈: {home}")
    print()

# Player 클래스 정의
class Player:
    def __init__(self, name, position, number):
        self.name = name
        self.position = position
        self.number = number
        self.selected = False

    def __str__(self):
        return f"이름: {self.name}, 포지션: {self.position}, 번호: {self.number}"

# selected_players.pkl 파일에서 선수 정보 가져오기
with open("selected_players.pkl", "rb") as file:
    players = list(pickle.load(file))

# 경기 진행
inning_count = 1
out_count = 0
doosan = 0

# 선수들의 결과 기록 초기화
player_results = {player: None for player in players}

# 메인 게임 루프
while out_count < 3:
    print('--------------------------------'*5)
    print('--------------------------------'*5)
    print(f"{inning_count}이닝 시작!")
    base1 = None
    base2 = None
    base3 = None
    home = None

    # 선수들 순환
    while players:
        selected_players = [player for player in players if player.selected]
        if len(selected_players) == len(players):
            break  # 모든 선수가 선택된 경우 게임 종료
        available_players = [player for player in players if not player.selected]
        player = random.choice(available_players)
        player.selected = True
        print(f"{player.name} 타석에 들어섰습니다.")
        strikes = 0

        # 타격 루프
        while strikes < 3:
            result = random.choice(["스트라이크", "헛스윙", "치다", "홈런", "볼"])
            print(f"{player.name}: {result}")

            # 결과 처리
            if result == "스트라이크" or result == "헛스윙":
                strikes += 1
                print("스트라이크!")
            elif result == "볼":
                print("볼!")
            elif result == "치다":
                hit_result = random.choice(["아웃", "플라이아웃", "1루타", "2루타", "3루타"])
                print(f"{player.name}: {hit_result}")

                if hit_result == "1루타":
                    if base3 is not None:
                        doosan += 1
                        base3 = None
                    if base2 is not None:
                        base3 = base2
                        base2 = None
                    if base1 is not None:
                        base2 = base1
                        base1 = None
                    base1 = player
                    strikes = 0
                elif hit_result == "2루타":
                    if base3 is not None:
                        doosan += 1
                        base3 = None
                    if base2 is not None:
                        doosan += 1
                        base2 = None
                    if base1 is not None:
                        base3 = base1
                        base1 = None
                    base2 = player
                    strikes = 0
                elif hit_result == "3루타":
                    if base3 is not None:
                        doosan += 1
                        base3 = None
                    if base2 is not None:
                        doosan += 1
                        base2 = None
                    if base1 is not None:
                        doosan += 1
                        base1 = None
                    base3 = player
                    strikes = 0
                elif hit_result == "아웃" or hit_result == "플라이아웃":
                    print(f"{player.name} 아웃!")
                    out_count += 1
                    break
            elif result == "홈런":
                doosan += 1
                if base1 is not None:
                    doosan += 1
                    base1 = None
                if base2 is not None:
                    doosan += 1
                    base2 = None
                if base3 is not None:
                    doosan += 1
                    base3 = None
                print(f"{player.name} 홈런!")

            # 각 타격 후 베이스 상황 출력
            basecall()

        if out_count >= 3:
            break

    # 이닝 종료 후 점수 출력
    print(f"{inning_count}이닝 종료!")
    print(f"두산: {doosan} 점")
    inning_count += 1

# 게임 종료
print("경기 종료!")

