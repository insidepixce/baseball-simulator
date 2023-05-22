import random

# 팀 이름과 선수들의 이름을 입력 받습니다.
team1_name = input("팀 1의 이름을 입력하세요: ")
team2_name = input("팀 2의 이름을 입력하세요: ")

team1_players = input("팀 1의 선수들의 이름을 쉼표로 구분하여 입력하세요: ").split(",")
team2_players = input("팀 2의 선수들의 이름을 쉼표로 구분하여 입력하세요: ").split(",")

# 이닝당 최대 아웃 수
MAX_OUTS = 3

# 이닝당 최대 점수
MAX_SCORE = 5

# 이닝 수
NUM_INNINGS = 9

# 팀 점수 초기화
team1_score = 0
team2_score = 0

# 경기 진행
for inning in range(1, NUM_INNINGS + 1):
    print("=== {} 이닝 ===".format(inning))
    outs = 0
    team_at_bat = 1

    while outs < MAX_OUTS:
        if team_at_bat == 1:
            player = random.choice(team1_players)
            print("{}(이)가 타석에 들어섭니다.".format(player))
        else:
            player = random.choice(team2_players)
            print("{}(이)가 타석에 들어섭니다.".format(player))

        # 타격 결과 계산
        hit_result = random.choice(["안타", "아웃", "홈런"])
        if hit_result == "안타":
            print("안타! 타자가 진루합니다.")
            if team_at_bat == 1:
                team1_score += 1
            else:
                team2_score += 1
        elif hit_result == "아웃":
            print("아웃!")
            outs += 1
        else:
            print("홈런! 타자가 홈을 밟습니다.")
            if team_at_bat == 1:
                team1_score += 1
            else:
                team2_score += 1

        # 팀 교체
        team_at_bat = 2 if team_at_bat == 1 else 1

        # 이닝 종료 확인
        if team_at_bat == 1 and outs == MAX_OUTS:
            break

    print("=== {} 이닝 종료 ===".format(inning))
    print("{}: {}점, {}: {}점".format(team1_name, team1_score, team2_name, team2_score))

    # 경기 종료 조건 확인
    if inning == NUM_INNINGS and team1_score != team2_score:
        break

# 최종 스코어 출력
print("=== 경기 종료 ===")
print("{}: {}점, {}: {}점".format(team1_name, team1_score, team2_name, team2_score))
if team1_score > team2_score:
    print("{}(이)가 승리하였습니다!".format(team1_name))
elif team1_score < team2_score:
    print("{}(이)가 승리하였습니다!".format(team2_name))
else:
    print("무승부입니다.")
