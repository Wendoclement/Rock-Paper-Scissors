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
defeats_dict = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
}

Win condition: If player 1's choice defeats Player 2's choice, Player 1 wins.
Loss condition: If player 2's choice is not defeated by player 1's choice, Player 2 wins.

## Code Structure
```python
get_player_choice(player_number):
Prompts a player for their choice and validates the input.

```python
ask_play_again()
Asks players if they want to restart the game and validates the response

```python
play_game()
This is the main loop.
````
