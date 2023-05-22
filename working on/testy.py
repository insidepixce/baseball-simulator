import random
import pickle

class Player:
    def __init__(self, name):
        self.name = name

class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = [Player(name) for name in players]
        self.score = 0
        self.bases = [None, None, None]

class Game:
    MAX_OUTS = 3
    NUM_INNINGS = 9

    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.strike_counts = {player: 0 for player in self.team1.players + self.team2.players}
        self.player_results = {player: None for player in self.team1.players + self.team2.players}

    def update_bases(self, hit_result, current_player, current_team):
        if hit_result == "1루타":
            if current_team.bases[0] is not None:
                current_team.bases[1] = current_team.bases[0]
            current_team.bases[0] = current_player

        elif hit_result == "2루타":
            if current_team.bases[0] is not None:
                current_team.bases[2] = current_team.bases[0]
                current_team.bases[0] = None
            if current_team.bases[1] is not None:
                current_team.bases[2] = current_team.bases[1]
                current_team.bases[1] = None
            current_team.bases[1] = current_player

        elif hit_result == "3루타":
            if current_team.bases[0] is not None:
                current_team.score += 1
                current_team.bases[0] = None
            if current_team.bases[1] is not None:
                current_team.score += 1
                current_team.bases[1] = None
            if current_team.bases[2] is not None:
                current_team.score += 1
                current_team.bases[2] = None
            current_team.bases[2] = current_player

        self.print_bases(current_team)

    def print_bases(self, current_team):
        # 베이스 상황 출력
        print("Bases after the play:")
        print(f"1루: {current_team.bases[0]}")
        print(f"2루: {current_team.bases[1]}")
        print(f"3루: {current_team.bases[2]}")
        print()

    def play_inning(self, team_at_bat):
        outs = 0
        players = team_at_bat.players.copy()  # 카피해서 사용

        while outs < self.MAX_OUTS and players:
            current_player = players.pop(0)


            while self.strike_counts[current_player] < 3:
                result = random.choice(["스트라이크", "헛스윙", "치다", "홈런", "볼"])
                print(f"{current_player.name}가 {result} 했습니다.")
                if result == "스트라이크" or result == "헛스윙":
                    self.strike_counts[current_player] += 1
                elif result == "치다":
                    hit_result = random.choice(["아웃", "플라이아웃", "1루타", "2루타", "3루타"])
                    print(f"{current_player.name}가 {hit_result} 했습니다.")
                    if hit_result in ["1루타", "2루타", "3루타"]:
                        self.update_bases(hit_result, current_player, team_at_bat)
                        break
                    else:
                        print(f"{current_player.name} - {hit_result}!")
                        outs += 1
                        break
                elif result == "홈런":
                    print(f"{current_player.name} - 홈런!")
                    for i in range(3):
                        if team_at_bat.bases[i] is not None:
                            team_at_bat.score += 1
                            team_at_bat.bases[i] = None
                            print("선수가 홈으로 들어갔습니다.")
                            print(f"{team_at_bat.name}에 한 점!")
                    team_at_bat.score += 1
                    break

        self.strike_counts = {player: 0 for player in team_at_bat.players}

    def play(self):
        for inning in range(1, self.NUM_INNINGS + 1):
            print(f"=== {inning} 이닝 ===")
            self.play_inning(self.team1)
            self.play_inning(self.team2)
            print(f"=== {inning} 이닝 종료 ===")
            print(f"{self.team1.name}: {self.team1.score}점, {self.team2.name}: {self.team2.score}점")

def load_teams():
    try:
        with open('teams.pickle', 'rb') as f:
            teams = pickle.load(f)
    except FileNotFoundError:
        teams = []

    return teams

def save_teams(teams):
    with open('teams.pickle', 'wb') as f:
        pickle.dump(teams, f)

def get_teams():
    teams = load_teams()
    if not teams:
        team1_name = input("팀 1의 이름을 입력하세요: ")
        team1_players = input("팀 1의 선수들의 이름을 쉼표로 구분하여 입력하세요: ").split(",")
        team2_name = input("팀 2의 이름을 입력하세요: ")
        team2_players = input("팀 2의 선수들의 이름을 쉼표로 구분하여 입력하세요: ").split(",")

        team1 = Team(team1_name, team1_players)
        team2 = Team(team2_name, team2_players)

        teams = [team1, team2]
        save_teams(teams)

    return teams

def main():
    teams = get_teams()
    team1 = teams[0]
    team2 = teams[1]

    game = Game(team1, team2)
    game.play()

if __name__ == "__main__":
    main()
