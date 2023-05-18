from batters_position import player_dict
import pickle

players = []
selected_players = set()

while len(selected_players) < 9:
    name = input("선수를 입력하세요 (선수 번호 또는 이름): ")

    found_players = [player for player in player_dict.values() if player.name == name]

    if len(found_players) == 0:
        print("선택한 선수가 없습니다. 다시 선택하세요.")
    elif len(found_players) > 1:
        print("중복된 선수가 있습니다. 다시 선택하세요.")
    else:
        player = found_players[0]
        if player in selected_players:
            print("이미 선택한 선수입니다. 다른 선수를 선택하세요.")
        else:
            players.append(player)
            selected_players.add(player)
            print(f"{player.position} {player.name} 선수가 추가되었습니다.")

print("선수 선택이 완료되었습니다.")
print()
lineup = selected_players

# 선수 선택이 완료된 이후에 피클 파일 생성
with open('selected_players.pkl', 'wb') as file:
    pickle.dump(lineup, file)
