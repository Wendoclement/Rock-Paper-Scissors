from enum import Enum, auto
from typing import Dict, Optional, Tuple

class Move(Enum):
    """
    Possible Moves in the game.
    """
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()

    def __str__(self):
        return self.name.capitalize()
    
class Player:
    """
    Class to represent a player in the game with a name and score tracking.
    """
    def __init__(self,name:str)->None:
        self.name = name
        self.score = 0
        self.current_move: Optional[Move] = None

    def choose_move(self) -> None:
        """
        It prompts the player to choose a new move.
        """
        print(f"\n{self.name}'s turn: ")
        for index, move in enumerate(Move,start=1):
            print(f"{index}. {move}")

        while True:
            try:
                choice = int(input("Enter your move (1-3): "))
                if 1<= choice <=3:
                    self.current_move = list(Move)[choice-1]
                    break
                print("Invalid choice! Please enter a number between 1 and 3.")
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 3.")

class Game:
    """A class to manage the game logic and flow."""
    def __init__(self)->None:
        self.players = [
            Player(input("Enter Player 1's name: ")),
            Player(input("Enter Player 2's name: "))
        ]
        self.round = 0
        self.wins_conditions: Dict[Tuple[Move, Move], str] = {
            (Move.ROCK, Move.SCISSORS ):"Rock crushes Scissors",
            (Move.PAPER, Move.ROCK):"Paper covers Rock",
            (Move.SCISSORS, Move.PAPER):"Scissors cuts Paper",
        }
    def determine_winner(self) -> Optional[Player]:
        """Determining the winner of the current round"""
        p1_move, p2_move = self.players[0].current_move, self.players[1].current_move

        if p1_move == p2_move:
            return None
        
        for (winner_move, loser_move), message in self.wins_conditions.items():
            if p1_move == winner_move and p2_move == loser_move:
                return self.players[0]
            elif p2_move == winner_move and p1_move == loser_move:
                return self.players[1]
        
        raise ValueError("Invalid move combination")
    
    def play_round(self) -> None:
        """This executes a single round of the game"""
        self.round += 1
        print(f"\n===Round {self.round}===")

        for player in self.players:
            player.choose_move()
            print(f"{player.name} chose {player.current_move}")

        winner = self.determine_winner()

        if winner:
            winner.score += 1
            print(f"\n{winner.name} wins this round!")
        else:
            print("\nIt's a tie!")    
        
        self.display_scores()

    def display_scores(self) -> None:
        """Display the current scores of both players"""
        print("\nCurrent Scores:")
        for player in self.players:
            print(f"{player.name}: {player.score}")

    def play_game(self)->None:
        """Manages the complete game flow"""
        print("\n=== Rock, Paper, Scissors Game ===")
        print("Best of 3 rounds wins!")
        print("Choose your moves wisely!")

        while max(p.score for p in self.players) < 2:
            self.play_round()
            print("\n")

        winner = max(self.players, key=lambda p: p.score)
        print(f"Congratulations {winner.name}! You are the overall winner!")

if __name__ == "__main__":
    game = Game()
    game.play_game()   