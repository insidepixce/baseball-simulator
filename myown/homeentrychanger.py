hbatter_dict = {}
with open("hometeam_entry_list.txt", "r") as file:
    lines = file.readlines()
    for i in range(9):
        line = lines[i].strip()  # 줄바꿈 문자 제거
        info = line.split(", ")  # 쉼표와 공백으로 분리
        name = info[0][6:]  # "Name: " 이후의 문자열 추출
        position = info[1][10:]  # "Position: " 이후의 문자열 추출
        number = int(info[2][8:])  # "Number: " 이후의 문자열 추출하여 정수로 변환
        hbatter_dict[f"hbatter{i+1}"] = (name, position, number)

print(hbatter_dict["hbatter1"])
print(hbatter_dict[f"hbatter{i+1}"][0])
