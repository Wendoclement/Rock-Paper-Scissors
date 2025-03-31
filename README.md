# Rock-Paper-Scissors Game

A simple Python implementation of the classic Rock-Paper-Scissors game for two players.

## Description

Two player terminal game for Rock-Paper-Scissors. The game has a robust input validation framework, a cuttng edge winner determination logic, and the option to play again after each round.

## How to Play

1. **Player 1** and **Player 2** take turns entering their choices (Rock, Paper, or Scissors).
2. The game compares the choices using a predefined ruleset:
   - Rock beats Scissors
   - Scissors beats Paper
   - Paper beats Rock
3. If both players choose the same option, it's a tie.
4. After each round, players can choose to play again or exit.

## Algorithm Explanation

The winner determination uses a dictionary (`defeats_dict`) to map each choice to the option it defeats:

````python
#convert possible outcomes in terms of (0,1,2)
such that:
  rock==0
  scissors==1
  paper==2
draw possible outcomes for the game:
(x,y)
(0,0)
(0,1)
(0,2)
(1,0)
(1,1)
(1,2)
(2,0)
(2,1)
(2,2)
Recall for a tie, then (x=y)
for player 2 win :
    (0,1)
    (2,0)
    (1,2)
else:
 player 1 wins
#this is good but wont cover possible scenarios

defeats_dict = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
}

Win condition: If player 1's choice defeats Player 2's choice, Player 1 wins.
#how 
Loss condition: If player 2's choice is not defeated by player 1's choice, Player 2 wins.

get_player_choice(player_number):
Prompts a player for their choice and validates the input.(random inputs )

ask_play_again()
Asks players if they want to restart the game and validates the response

play_game()
This is the main loop.
````
