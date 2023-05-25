import random
from homeentrychanger import hbatter_dict

def throw_a_ball(hbatter_dict):
        first_player=next(iter(hbatter_dict))
        name, position, number = hbatter_dict[first_player]
        throwball = random.choice(["치다", "헛스윙", "스트라이크", "볼"])
        print(f"{name}({position}, {number}) - {throwball}")

throw_a_ball(hbatter_dict)


def throw_a_ball2(hbatter_dict):
        second_player=next(iter(hbatter_dict))
        name, position, number = hbatter_dict[second_player]
        throwball = random.choice(["치다", "헛스윙", "스트라이크", "볼"])
        print(f"{name}({position}, {number}) - {throwball}")

throw_a_ball(hbatter_dict)
throw_a_ball2(hbatter_dict)



"""
출력값 
양의지(포수, 25) - 스트라이크
김재환(외야수, 32) - 볼
이유찬(내야수, 7) - 헛스윙
강승호(내야수, 23) - 헛스윙
허경민(내야수, 13) - 볼
정수빈(외야수, 31) - 볼
안갈비(내야수, 3) - 스트라이크
로하스(외야수, 11) - 헛스윙
양석환(내야수, 53) - 헛스윙
 """

 #위 코드에서는 딕셔너리를 순회하면서 각 선수의 정보를 추출한다
 #그리고 random.choice()함수를 사용하여 각 선수에게 랜덤한 "throwwball"을 부여하고 출력핟다
 #전부다 넣지 않고 한명씩 할 수 있는 방법은 없을까?

 