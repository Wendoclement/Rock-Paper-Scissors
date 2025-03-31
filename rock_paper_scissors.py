from pprint import pprint

def get_player_choice(player_number):
    while True:
        name = input(f'Player {player_number},What is your name? ').strip().capitalize()
        if not name:
            print('Name cannot be empty!')
            continue

        choice = input(f"{name}, what's your choice (Rock, Paper, Scissors)? ").lower()

        if choice in ['rock','paper','scissors']:
            return choice,name
        print("Invalid input, choose between Rock, Paper and Scissors")

def ask_play_again():
    while True:
        answer = input('Do you want to play again? (Yes/No): ').lower()
        if answer in ['yes','no']:
            return answer == 'yes'
        pprint('Invalid input! Kindly enter yes/no')   

def play_game():
    """
    Parent Function which invokes the input functions in an iteration.
    This functions contains the algorithm for determining the winner and losers
    """
    pprint('Welcome to Rock(🪨) Paper(🗒️) Scissors(✂️)')

    # Score tracking
    game_score = {}

    while True:
        p1_choice, p1_name = get_player_choice(1)
        p2_choice, p2_name = get_player_choice(2)

        if p1_name not in game_score:
            game_score[p1_name] = 0
        if p2_name not in game_score:
            game_score[p2_name] = 0

        defeats_dict = {
            'rock':'scissors',
            'paper':'rock',
            'scissors':'paper',
        }

        print(f"\n{p1_name} chose {p1_choice}, {p2_name} chose {p2_choice}")

        if p1_choice==p2_choice:
            pprint('It is a tie')
        else:
            if defeats_dict[p1_choice] == p2_choice:
                pprint(f'{p1_name} wins')
                game_score[p1_name]+=1
            
            else:
                pprint(f'{p2_name} wins')
                game_score[p2_name]+=1
        print("\n")
        pprint("Current scores:")
        pprint(game_score)

        if not ask_play_again():
            print('\nThanks for playing! Adios👻')
            break

if __name__ == "__main__":
    play_game()