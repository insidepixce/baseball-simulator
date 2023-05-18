from typing import List  # 타입 힌트용
from classis import Player  # 타입 힌트용
from batters_position import player_dict
import pickle
import json  # 데이터 시각화용

"""
수정 내용:
- 입력 도메인 추가: 선수 이름 -> 선수 이름 || 선수 벊
- 관리 시스템 전체를 선수 번호 기준으로 관리되도록 변경 (필요하다면 문자열 기반의 시스템으로 변경해도 무관)

* batters_position.py의 player_dict로 사용하는 것도 좋을 듯 (filter, map, sorted/sort 함수와 함께 사용하면 크게 문제 없음)
* 그게 아니라면 set을 쓰거나 dict를 쓰거나 하나만.
"""

players: List[Player] = []

# TODO: 가급적이면 while 조건에서 선수 수를 제한하는 것이 아닌, while은 무한 반복으로 돌리고 반복문 내에서 경고를 주도록 처리하는 것이 사용자 경험 측면에서 더 좋음
while len(players) < 9:
    name: str = input("선수를 입력하세요 (선수 번호 또는 이름): ").strip()

    # -> 번호 반영 안 됨 -> 번호와 이름 모두 반영되도록 수정
    # found_players = [player for player in player_dict.values() if player.name == name]
    found_players = list(filter(
        # -> "이름 또는 번호가 같으면"
        lambda p: p.name == name or str.isdigit(name) and p.number == int(name),
        player_dict.values()
    ))

    if len(found_players) == 0:
        print("선택한 선수가 없습니다. 다시 선택하세요.")
    elif len(found_players) > 1:
        print("중복된 선수가 있습니다. 다시 선택하세요.")
    else:
        player = found_players[0]
        # 기존: player in selected_players
        # set에는 원시자료형만 저장할 수 있어서 객체랑 집합 내에 있는 것을 in으로 비교하면
        # 의미가 없음
        if player.number in map(lambda p: p.number, players):
            print("이미 선택한 선수입니다. 다른 선수를 선택하세요.")
        else:
            players.append(player)
            # selected_players.add(player.number) 코드 제거
            print(f"{player.position} {player.name} 선수가 추가되었습니다.")

print("선수 선택이 완료되었습니다.")
print(f"저장된 데이터:\n{json.dumps(players, sort_keys=True, indent=4)}")

# 선수 선택이 완료된 이후에 피클 파일 생성
with open('selected_players.pkl', 'wb') as file:
    pickle.dump(list(map(lambda player: player.__dict__, players)), file)
