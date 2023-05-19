from typing import List, Dict, Union
from classis import Player, Players

"""
수정 내용:
- 입력 도메인 추가: 선수 이름 -> 선수 이름 || 선수 번호
- 관리 시스템 전체를 선수 번호 기준으로 관리되도록 변경 (필요하다면 문자열 기반의 시스템으로 변경해도 무관)

* batters_position.py의 player_dict로 사용하는 것도 좋을 듯 (filter, map, sorted/sort 함수와 함께 사용하면 크게 문제 없음)
* 그게 아니라면 set을 쓰거나 dict를 쓰거나 하나만.
"""

player_dict: list[Player] = [
    Player("허경민", "내야수", 13, False),
    Player("안승한", "포수", 20, False),
    Player("장승현", "포수", 22, False),
    Player("양의지", "포수", 25, False),
    Player("박유연", "포수", 26, False),
    Player("윤준호", "포수", 96, False),
    Player("안갈비", "내야수", 3, False),
    Player("신성현", "내야수", 5, False),
    Player("이유찬", "내야수", 7, False),
    Player("박계범", "내야수", 14, False),
    Player("서예일", "내야수", 16, False),
    Player("김민혁", "내야수", 18, False),
    Player("강승호", "내야수", 23, False),
    Player("권민석", "내야수", 34, False),
    Player("전민재", "내야수", 35, False),
    Player("김재호", "내야수", 52, False),
    Player("양석환", "내야수", 53, False),
    Player("임서준", "내야수", 93, False),
    Player("송승환", "외야수", 8, False),
    Player("로하스", "외야수", 11, False),
    Player("정수빈", "외야수", 31, False),
    Player("김재환", "외야수", 32, False),
    Player("김대한", "외야수", 37, False),
    Player("김인태", "외야수", 39, False),
    Player("홍성호", "외야수", 44, False),
    Player("강진성", "외야수", 49, False),
    Player("조수행", "외야수", 51, False),
    Player("양찬열", "외야수", 57, False)

