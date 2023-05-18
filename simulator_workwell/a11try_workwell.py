import random
import pickle

# Player 클래스 정의
class Player:
    def __init__(self, name, position, number):
        self.name = name
        self.position = position
        self.number = number

    def __str__(self):
        return f"이름: {self.name}, 포지션: {self.position}, 번호: {self.number}"

# selected_players.pkl 파일에서 선수 정보 가져오기
with open("selected_players.pkl", "rb") as file:
    players = list(pickle.load(file))

# 경기 진행
print("경기를 시작합니다 ----------------))))")
inning_count = 0
game_over = False
player_index = 0
home_score = 0  # 홈팀 점수 초기화
while not game_over:       
    inning_count += 1           
    print(f"{inning_count}이닝 시작!")
    out_count = 0
    bases = [None, None, None, None]
    while out_count < 3:
        player_index = (player_index + 1) % len(players)
        current_player = players[player_index]
        print(f"\n{current_player.name}({current_player.number}번 타자)가 타석에 들어섰습니다.")
        play_result = random.choice(["안타", "아웃", "홈런"])
        if play_result == "안타":
            print(f"{current_player.name}({current_player.number}번 타자)가 안타를 칩니다.")
            for i in range(3, 0, -1):
                if bases[i] is not None:
                    bases[i] = None
                    if i + 1 <= 3:
                        bases[i + 1] = current_player
                    else:
                        bases[3] = current_player
            bases[1] = current_player
        elif play_result == "아웃":
            print(f"{current_player.name}({current_player.number}번 타자)가 아웃되었습니다.")
            out_count += 1
        elif play_result == "홈런":
            print(f"{current_player.name}({current_player.number}번 타자)가 홈런을 칩니다.")
            for i in range(3, 0, -1):
                if bases[i] is not None:
                    bases[i] = None
                    bases[3] = current_player
            bases[3] = current_player
            home_score += 1  # 홈팀 점수 추가
        print("베이스 상황:", end=" ")
        for i in range(1, 4):
            if bases[i] is not None:
                print(f"{bases[i].name}({bases[i].number}번)", end=" ")
            else:
                print("주자 없음", end=" ")
        print()
    print(f"{inning_count}이닝 종료!")
    print(f"홈팀 점수: {home_score}점\n")
    if inning_count == 9:
        game_over = True
        print("경기 종료!")
        
# 경기 결과 출력
print(f"최종 점수: 홈팀 {home_score}점")
