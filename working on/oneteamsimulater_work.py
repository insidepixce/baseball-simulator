import random

class Inning:
    def __init__(self):
        self.outs = 0
        self.runs = 0
        self.bases = [None, None, None, None]

    def player_hit(self, player, hit_base):
        # hit_base에 따라 진루시킵니다.
        if hit_base == 4:  # 홈런인 경우
            for i in range(1, 4):  # 기존의 베이스에 선수가 있다면 홈으로 진루
                if self.bases[i] is not None:
                    self.runs += 1
                    self.bases[i] = None
            self.runs += 1  # 홈런친 선수도 점수에 포함
        else:  # 안타인 경우
            for i in range(3, 0, -1):  # 3루부터 1루까지 거꾸로 진루
                if self.bases[i] is not None:
                    if i + hit_base >= 4:  # 진루하려는 베이스가 홈인 경우
                        self.runs += 1
                    else:  # 홈이 아니면 진루
                        self.bases[i + hit_base] = self.bases[i]
                    self.bases[i] = None  # 기존의 베이스는 비웁니다.
            self.bases[hit_base] = player  # 새로운 선수를 베이스에 위치시킵니다.

        # 베이스 상황을 출력합니다.
        self.print_bases()
        # 점수를 출력합니다.
        print('현재 점수:', self.runs, '점 입니다.\n')

    def out(self, player):
        print(f'{player} 선수가 아웃되었습니다.')
        self.outs += 1
        # 아웃 카운트를 출력합니다.
        print('아웃 카운트:', self.outs, '\n')
        if self.outs == 3:
            print('세 아웃! 다음 이닝으로 넘어갑니다.\n')
            self.new_inning()

    def new_inning(self):
        self.bases = [None, None, None, None]
        self.outs = 0

    def print_bases(self):
        # 베이스 상황을 출력합니다.
        print('베이스 상황:')
        for i in range(1, 4):
            if self.bases[i] is not None:
                print(f'{i}루:', self.bases[i])
            else:
                print(f'{i}루: 비어있음')
        print()


def play_game():
    players = input('선수 이름을 입력해주세요 (쉼표로 구분): ').split(',')
    inning = Inning()
    inning_count = 1
    while inning_count <= 9:
        print(f'{inning_count}회초 이닝!')
        player_index = 0
        inning.new_inning()  # 이닝 시작 시 베이스와 아웃 카운트를 초기화
        while inning.outs < 3:  # 3아웃이 될 때까지 반복
            player = players[player_index]
            action = random.choice(['out', '1루타', '2루타', '3루타', '홈런'])
            print(f'{player}의 타석입니다!')
            print('어떤 공을 쳤을까요?', action, '이네요!')
            if action == 'out':
                inning.out(player)
                print(f'{player}이 아웃당했습니다!')
            elif action == '홈런':
                inning.player_hit(player, 4)
                print(f'{player}이 홈런을 쳤습니다!')
            elif action == '2루타':
                inning.player_hit(player, 2)
                print(f'{player}이 2루타를 쳤습니다!')
            else:
                inning.player_hit(player, 0)
            player_index = (player_index + 1) % len(players)  # 다음 선수로 변경

        if inning_count == 9 and inning.outs == 3:
            break

        print(f'{inning_count}회말 이닝!')
        player_index = 0
        inning.new_inning()  # 이닝 시작 시 베이스와 아웃 카운트를 초기화
        while inning.outs < 3:  # 3아웃이 될 때까지 반복
            player = players[player_index]
            action = random.choice(['out', '1루타', '2루타', '3루타', '홈런'])
            print(f'{player}의 타석입니다!')
            print('어떤 공을 쳤을까요?', action, '이네요!')
            if action == 'out':
                inning.out(player)
                print(f'{player}이 아웃당했습니다!')
            elif action == '홈런':
                inning.player_hit(player, 4)
                print(f'{player}이 홈런을 쳤습니다!')
            elif action == '2루타':
                inning.player_hit(player, 2)
                print(f'{player}이 2루타를 쳤습니다!')
            else:
                inning.player_hit(player, 0)
            player_index = (player_index + 1) % len(players)  # 다음 선수로 변경

        inning_count += 1

    print('게임이 종료되었습니다.')


if __name__ == '__main__':
    play_game()
