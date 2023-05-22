""" update1
name_or_number 변수를 picking_tool_for_home 함수 내에서 입력 받도록 수정합니다.
found 변수를 도입하여 선수를 찾았는지 여부를 추적합니다.
for 루프를 중첩하지 않고 하나의 반복문으로 수정합니다.
선수를 찾은 경우 found를 True로 설정하고 break 문을 사용하여 반복문을 종료합니다.
선수를 찾지 못한 경우 found가 False인 상태이므로 "선수를 찾을 수 없습니다. 다시 선택하세요."를 출력합니다 """

from playerlist import player_dict

hometeam_final_entry = []

def picking_tool_for_home():
    for i in range(9):
        name_or_number = input("선수 이름 또는 번호를 입력하세요: ")
        found = False  # 선수를 찾았는지 여부를 나타내는 변수
        for hindi_player in player_dict:
            if hindi_player.name == name_or_number:
                hometeam_final_entry.append(hindi_player)
                print("{}번째 선수는".format(i+1), hometeam_final_entry[i].name, hometeam_final_entry[i].position, "입니다.")
                found = True
                break
        if not found:
            print("선수를 찾을 수 없습니다. 다시 선택하세요.")

picking_tool_for_home()

with open("hometeam_entry_list.txt", "w") as file:
    for player in hometeam_final_entry:
        file.write(str(player) + "\n")
