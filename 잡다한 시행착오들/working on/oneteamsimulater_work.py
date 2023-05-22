import random

def save_output(outputlist, outputs):
    with open(outputlist, 'w') as file:
        for output in outputs:
            file.write(output + '\n')
                 
class Inning:
    def __init__(self):
        self.outs = 0
        self.runs = 0
        self.bases = [None, None, None, None]
    
    def new_inning(self):
        self.bases = [None, None, None, None]
        self.outs = 0
        self.runs = 0
        
    def ball(self):
        print('볼!')

    def player_hit(self, player, hit_base):
        if hit_base == 4:
            for i in range(1, 4):
                if self.bases[i] is not None:
                    self.runs += 1
                    self.bases[i] = None
            self.runs += 1
        else:
            for i in range(3, 0, -1):
                if self.bases[i] is not None:
                    if i + hit_base >= 4:
                        self.runs += 1
                    else:
                        self.bases[i + hit_base] = self.bases[i]
                    self.bases[i] = None
            self.bases[hit_base] = player

        self.print_bases()
        print('현재 점수:', self.runs, '점 입니다.\n')

    def strike(self):
        if not hasattr(self, 'strike_counts'):
            self.strike_counts = 0
        self.strike_counts += 1
        print('스트라이크 카운트:', self.strike_counts)
        print('아웃 카운트:', self.outs)
        if self.strike_counts == 3:
            print('삼진 아웃! 다음 타자가 타석에 입장합니다.\n')
            self.outs += 1
            self.strike_counts = 0


    def ball(self):
        print('볼!')

    def out(self):
        self.outs += 1
        print('아웃!', '아웃 카운트:', self.outs)
        if self.outs == 3:
            print('세 아웃! 다음 이닝으로 넘어갑니다.\n')
            self.new_inning()

    def new_inning(self):
        self.bases = [None, None, None, None]
        self.outs = 0

    def print_bases(self):
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
    outputs = []
    while inning_count <= 9:
        outputs.append(f'\n\n----------{inning_count}번째 이닝!')
        player_index = 0
        inning.new_inning()
        while inning.outs < 3:
            player = players[player_index]
            action = random.choice(['strike', 'ball', 'hit'])
            outputs.append(['\n', f'{player}의 타석입니다!', '어떤 공을 쳤을까요?', action + " 이네요!"])
            if action == 'strike':
                inning.strike()
            elif action == 'ball':
                inning.ball()
            else:
                hit_base = random.choice([0, 1, 2, 3, 4])
                if hit_base == 0:
                    inning.out()
                else:
                    inning.player_hit(player, hit_base)
                    outputs.append([f'{player}이 {hit_base}루타를 쳤습니다!'])

            player_index = (player_index + 1) % len(players)

        if inning_count < 9:
            input("\n다음 이닝으로 넘어가려면 엔터 키를 누르세요.")
            print()

        inning_count += 1

    outputs.append("게임이 종료되었습니다.")
    return outputs

def save_output(outputlist, outputs):
    with open(outputlist, 'w') as file:
        for output_group in outputs:
            if isinstance(output_group, list):
                file.write('\n'.join(output_group) + '\n')
            else:
                file.write(str(output_group) + '\n')



if __name__ == "__main__":
    print("게임을 시작합니다!")
    output_filename = 'game_output.txt'
    game_outputs = play_game()
    save_output(output_filename, *outputs)
