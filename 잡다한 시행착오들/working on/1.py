import random

class Inning:
    # Rest of the class code...

    def play_game():
        players = input('선수 이름을 입력해주세요 (쉼표로 구분): ').split(',')
        inning = Inning()

        for i in range(9):
            print(f'{i+1}번째 이닝!')
            player_index = 0
            while inning.outs < 3:
                player = players[player_index]
                action = random.choice(['out', '1루타', '2루타', '3루타', '홈런'])
                print('액션:', action)
                if action == 'out':
                    inning.out(player)
                elif action == '홈런':
                    inning.player_hit(player, 4)
                else:
                    hit_base = int(action[0])
                    inning.player_hit(player, hit_base)
                player_index = (player_index + 1) % len(players)
            inning.new_inning()

    if __name__ == "__main__":
        play_game()





