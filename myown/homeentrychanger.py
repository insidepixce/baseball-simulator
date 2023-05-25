hbatter_dict = {}
with open("/Volumes/samsick/baseballpython/myown/hometeam_entry_list.txt", "r") as file:
    lines = file.readlines()
    for i in range(9):
        line = lines[i].strip()  # 줄바꿈 문자 제거
        info = line.split(", ")  # 쉼표와 공백으로 분리
        name = info[0][6:]  # "Name: " 이후의 문자열 추출
        position = info[1][10:]  # "Position: " 이후의 문자열 추출
        number = int(info[2][8:])  # "Number: " 이후의 문자열 추출하여 정수로 변환
        hbatter_dict[f"hbatter{i+1}"] = (name, position, number)

import random


#주어진 코드는 "hometeam_entry_list.txt"파일에서 선수 정보를 읽어와 
#hbatter-dict를 구성하는 코드이다
#각 줄에서 선수의 이름, 포지션, 번호를 추출하여 추가한다
#이름을 키로 갖고, 해당 선수의 정보를 튜플로 가지는 딕셔너리이다 
