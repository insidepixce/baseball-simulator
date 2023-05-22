import random
import pickle

with open('selected_players.pkl', 'rb') as f:
    lineup = pickle.load(f)

# 팀 정보
teams = ['두산베어스', 'NC다이노스']
team_a_score = 0
team_b_score = 0

# 이닝 정보
inning = 1
outs = 0
max_outs = 3

# 게임 진행
while inning <= 9:  # 총 9이닝까지 진행
    print(f'\n{inning} 이닝 시작!')
    print('----------------------------------------이닝이 시작됩니다--------------------------------------------\n--\n-')

    # 이닝 내 루 정보
    bases = [False, False, False]

    # 아웃 처리
    while outs < max_outs:
        print(f'현재 아웃: {outs}')

        # 랜덤한 타자 결과 처리 (예시)
        hit_result = random.choice(['out', 'single', 'double', 'triple', 'home_run'])
        player_result = random.choice(lineup)

        if ":" in player_result:
            selected_player = player_result.split(": ")[0]
            selected_position = player_result.split(": ")[1]
            # 타자 결과에 따른 처리
            if hit_result == 'out':
                outs += 1
                print('아웃!')
            elif hit_result == 'single':
                if bases[2]:  # 3루에 주자 있을 경우 득점
                    if random.random() <= 0.5:
                        team_a_score += 1
                    else:
                        team_b_score += 1
                    bases[2] = False
                bases[2] = bases[1]
                bases[1] = bases[0]
                bases[0] = True
                print('안타!')
            elif hit_result == 'double':
                if bases[2]:
                    if random.random() <= 0.5:
                        team_a_score += 1
                    else:
                        team_b_score += 1
                if bases[1]:
                    if random.random() <= 0.5:
                        team_a_score += 1
                    else:
                        team_b_score += 1
                bases[2] = bases[0]
                bases[1] = True
                bases[0] = False
                print('2루타!')
            elif hit_result == 'triple':
                if bases[2]:
                    if random.random() <= 0.5:
                        team_a_score += 1
                    else:
                        team_b_score += 1
                if bases[1]:
                    if random.random() <= 0.5:
                        team_a_score += 1
                    else:
                        team_b_score += 1
                if bases[0]:
                    if random.random() <= 0.5:
                        team_a_score += 1
                    else:
                        team_b_score += 1
                bases[2] = True
                bases[1] = False
                bases[0] = False
                print('3루타!')
            elif hit_result == 'home_run':
                if bases[2]:
                    if random.random() <= 0.5:
                        team_a_score += 1
                    else:
                        team_b_score += 1
                if bases[1]:
                    if random.random() <= 0.5:
                        team_a_score += 1
                    else:
                        team_b_score += 1
                if bases[0]:
                    if random.random() <= 0.5:
                        team_a_score += 1
                    else:
                        team_b_score += 1
                if random.random() <= 0.5:
                    team_a_score += 1
                else:
                    team_b_score += 1
                bases = [False, False, False]
                print('홈런!')
        else:
            print("선수 결과 형식이 잘못되었습니다.")

    # 한 이닝이 종료되면 아웃 카운트 초기화
    outs = 0

    # 다음 이닝으로 넘어가기 전에 현재 점수 출력
    print(f'\n{inning} 이닝 종료!')
    print('------------------------------')
    print(f'{teams[0]}: {team_a_score}점')
    print(f'{teams[1]}: {team_b_score}점')

    # 다음 이닝으로 진행
    inning += 1

# 최종 점수 출력
print('\n게임 종료!')
print('------------------------------')
print(f'{teams[0]}: {team_a_score}점')
print(f'{teams[1]}: {team_b_score}점')
