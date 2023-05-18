import pickle

with open('selected_players.pkl', 'rb') as file:
    saved_players = pickle.load(file)

# 저장된 선수들의 정보 출력
for player in saved_players:
    print(player.name, player.position, player.number)
    

for player in saved_players:
    print(player)
