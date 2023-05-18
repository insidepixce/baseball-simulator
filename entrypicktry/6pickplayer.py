import pickle
from batters_position import player_dict

lineup = []
player_names = [player.name for player in player_dict.values()]
player_numbers = [player.number for player in player_dict.values()]
player_positions= [player.position for player in player_dict.values()]

for i in range(1, 10):
    player_name = input(f'선수 {i}의 이름을 입력하세요: ')
    try:
        index = player_names.index(player_name)
        selected_player = player_names[index]
        selected_number = player_numbers[index]
        print(f'{selected_number}번 선수 {selected_player}가 {i}번 타자로 등록되었습니다.')
        lineup.append(selected_player)
    except ValueError:
        print('선수를 찾을 수 없습니다.')
        

# 선수들을 파일에 저장
with open('selected_players.pkl', 'wb') as file:
    pickle.dump(lineup, file)
