from typing import List, Dict, Union
from classis import Player, Players


player_list: List[Dict[str, Union[str, int, bool]]] = Players.to_list(
    [
        Player("허경민", "내야수", 13),
        Player("안승한", "포수", 20),
        Player("장승현", "포수", 22),
        Player("양의지", "포수", 25),
        Player("박유연", "포수", 26),
        Player("윤준호", "포수", 96),
        Player("안갈비", "내야수", 3),
        Player("신성현", "내야수", 5),
        Player("이유찬", "내야수", 7),
        Player("박계범", "내야수", 14),
        Player("서예일", "내야수", 16),
        Player("김민혁", "내야수", 18),
        Player("강승호", "내야수", 23),
        Player("권민석", "내야수", 34),
        Player("전민재", "내야수", 35),
        Player("김재호", "내야수", 52),
        Player("양석환", "내야수", 53),
        Player("임서준", "내야수", 93),
        Player("송승환", "외야수", 8),
        Player("로하스", "외야수", 11),
        Player("정수빈", "외야수", 31),
        Player("김재환", "외야수", 32),
        Player("김대한", "외야수", 37),
        Player("김인태", "외야수", 39),
        Player("홍성호", "외야수", 44),
        Player("강진성", "외야수", 49),
        Player("조수행", "외야수", 51),
        Player("양찬열", "외야수", 57)
    ]
)