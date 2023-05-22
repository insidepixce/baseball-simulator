import random

class Player:
    def __init__(self, name, position, number):
        self.name = name
        self.position = position
        self.number = number
        self.strike = 0  # 선수의 스트라이크 카운트
        self.hithit = 0  # 이 선수가 이번 이닝에서 안타를 친 횟수

class Inning:
    def __init__(self):
        self.bases = [None, None, None, None, None]  # 1루, 2루, 3루, 홈
        self.outs = 0  # 아웃 카운트
        self.score = 0  # 점수

    def player_hit(self, player, hit_base):
        print(f"{player.name} 선수가 {hit_base}루타를 쳤습니다.")
        # 타자가 안타를 치면 모든 베이스 상의 선수들이 hit_base만큼 전진
        for i in range(3, 0, -1):
            if i >= hit_base and self.bases[i-hit_base] is not None:
                if i == 3:
                    self.score += 1
                    print("득점! 현재 점수: ", self.score)
                self.bases[i] = self.bases[i-hit_base]
                self.bases[i-hit_base] = None
        self.bases[hit_base] = player
        player.hithit = 1

    def player_strike(self, player):
        player.strike += 1
        if player.strike == 3:
            self.player_out(player)
            player.strike = 0  # 선수의 스트라이크 카운트 초기화

    def player_out(self, player):
        print(f"{player.name} 아웃!")
        self.outs += 1
        if self.outs >= 3:  # 3아웃이면 이닝 종료
            self.end_inning()

    def end_inning(self):
        print("이닝 종료!")
        for player in self.bases:
            if player is not None:
                player.hithit = 0  # 모든 선수의 안타 카운트 초기화
        self.bases = [None, None, None, None]  # 베이스 초기화
        self.outs = 0  # 아웃 카운트 초기화

def play_game():
    players = []
    for i in range(1, 10):
        player_name = input(f"선수 {i}의 이름을 입력하세요: ")
        players.append(Player(player_name, "포지션"+str(i), i))

    for inning_number in range(1, 10):  # 게임을 9번 반복 (9이닝)
        print(f"\n{inning_number}번째 이닝 시작!")
        inning = Inning()
        for player in players:
            print(f"{player.name} 선수가 타석에 나왔습니다.")
            while True:
                action = random.randint(0, 4)
                if action == 0:  # 스트라이크
                    inning.player_strike(player)
                else:  # 1루타, 2루타, 3루타, 홈런
                    inning.player_hit(player, action)
                if inning.outs >= 3 or player.hithit == 1:
                    break
        print(f"{inning_number}번째 이닝 종료, 현재 점수: {inning.score}")

play_game()
