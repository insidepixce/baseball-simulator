import random
from homeentrychanger import hbatter_dict

def throw_a_ball1(hbatter_dict):
    player_number = 1
    for player, info in hbatter_dict.items():
        if info[2] == player_number:
            name, position, number = info
            throwball = random.choice(["치다", "헛스윙", "스트라이크", "볼"])
            print(f"{name}({position}, {number}) - {throwball}")
            return

def throw_a_ball2(hbatter_dict):
    player_number = 2
    for player, info in hbatter_dict.items():
        if info[2] == player_number:
            name, position, number = info
            throwball = random.choice(["치다", "헛스윙", "스트라이크", "볼"])
            print(f"{name}({position}, {number}) - {throwball}")
            return

def throw_a_ball3(hbatter_dict):
    player_number = 3
    for player, info in hbatter_dict.items():
        if info[2] == player_number:
            name, position, number = info
            throwball = random.choice(["치다", "헛스윙", "스트라이크", "볼"])
            print(f"{name}({position}, {number}) - {throwball}")
            return

throw_a_ball1(hbatter_dict)
throw_a_ball2(hbatter_dict)
throw_a_ball3(hbatter_dict)


#이랬는데 실행이 안됨..,,           

# throw_a_ball4(hbatter_dict)
# throw_a_ball5(hbatter_dict)
# throw_a_ball6(hbatter_dict)
# throw_a_ball7(hbatter_dict)
# throw_a_ball8(hbatter_dict)
# throw_a_ball9(hbatter_dict)

#----

# break 문은 반복문을 종료하기 때문에 다음 선수들의 결과가 출력되지 않는다


#-----
#두번째 선수를 선택하기 위해서는 첫 번째 선수를 이미 사용한 후에 댜음 선수를 선택해야함. 
#throw_a_ball 함수와 throw_a_ball2 함수에서 'next(iter(hbatter_dict))'를 호출하기 전에 next(iter(hbatter_dict))를 한번 더 호출하기


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

 