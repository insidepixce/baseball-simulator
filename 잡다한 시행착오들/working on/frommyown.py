import random

class before_start_game:
    def pick_hometeam():
        num_players = 9
        hometeam_names = []
        for i in range(num_players):
            #0부터 num_players-1까지의 정수를 생성하는 범위
            hometeam_names.append(input('홈팀의 타자 9명을 뽑아주세요'))