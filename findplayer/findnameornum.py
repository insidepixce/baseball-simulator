from batters import doosan_players

def get_name_by_number(number):
    if number in doosan_players:
        return doosan_players[number]
    else:
        return "그 이름으로는 등번호를 찾을 수 없습니다."

def get_number_by_name(name):
    for number, player_name in doosan_players.items():
        if player_name == name:
            return number
    return "그 등번호로는 이름을 찾을 수 없습니다."


reques = lambda : input("등번호나 이름을 입력하세요: ")
requ = reques()
if type(requ)==str:
    print(get_number_by_name(requ))
else:
    print(get_name_by_number(requ))
