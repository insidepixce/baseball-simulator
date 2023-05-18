import pickle
from batters_position import player_dict
from classis import Player

lineup = []

for i in range(1, 10):
    player_name = input(f'선수 {i}의 이름을 입력하세요: ')
    try:
        player = player_dict[player_name]
        lineup.append((player.name, player.position, player.number))
        print(f'{i}번 타자로 {player.number}번 선수 {player.name}가 등록되었습니다.')
    except KeyError:
        print('선수를 찾을 수 없습니다.')

# 선수들을 파일에 저장
with open('selected_players.pkl', 'wb') as file:
    pickle.dump(lineup, file)
