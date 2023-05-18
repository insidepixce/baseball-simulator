from typing import List, Union, Literal

import random
import pickle

from classis import Player, Players


# 이닝 후 베이스 상황 출력하는 함수
def basecall():
    print("이닝 종료 후 베이스 상황:")
    print(f"1루: {base1}")
    print(f"2루: {base2}")
    print(f"3루: {base3}")
    print(f"홈: {home}")
    print()

# Player 클래스 정의부 제거 (의존성은 하나만)
players: List[Player] = []  # entrypicker에서 선택된 선수 리스트
cloned_players: List[Player] = []  # selected 요소가 초기화된 리스트

# selected_players.pkl 파일에서 선수 정보 가져오기
with open("players.pkl", "rb") as file:
    pickled_players = pickle.load(file)  # 정상적으로 저장되었다면, list()를 사용하지 않아도 list로 저장됨

    if type(pickled_players) == list:
        players = Players.to_players(pickled_players)
        for player in players:
            player.selected = False
            cloned_players.append(player)

# 경기 진행
inning_count: int = 1
out_count: int = 0
doosan: int = 0


# 메인 게임 루프
while out_count < 3:
    print('-'*32*5)
    print('-'*32*5)
    print(f"{inning_count}이닝 시작!")
    base1 = None
    base2 = None
    base3 = None
    home = None

    # 선수들 순환
    # while players:  # players는 truthy 값 -> 무한 반복
    random.shuffle(cloned_players)
    for player in cloned_players:
        # selected_players = list(filter(lambda player: player.selected, cloned_players))
        
        # if len(selected_players) == len(cloned_players):
        #     break  # 모든 선수가 선택된 경우 게임 종료
        
        # available_players = list(filter(lambda player: not player.selected, cloned_players))
    
        # player = random.choice(available_players)
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

