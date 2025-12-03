import random
import pandas as pd

class SnakeAndLadder:
    def __init__(self):
        self.players = [f"player{i+1}"for i in range(4)]
        self.size_of_the_board = 16
        self.players_position = {player:0 for player in self.players}
        self.move_history = []
    

    def roll_dice(self):
        return random.randint(1,7)
    
    def move_player(self, player, dice):
        new_position = self.players_position[player] + dice
        if new_position > self.size_of_the_board:
            print(f"{player} cannot move beyond the board size")
            return self.players_position[player]
        print(f"{player} moves from {self.players_position[player]} to {new_position}")
        self.players_position[player] = new_position
        return new_position
    
    def play(self):
        print("starting the game")
        winner = 0 
        while not winner:
            for player in self.players:
                dice = self.roll_dice()
                pos = self.move_player(player,dice)
                self.move_history.append({
                    "Players": player,
                    "Dice Roll History": dice,
                    "Postion History": pos,
                    "Win Status": 1 if pos == self.size_of_the_board else 0
                })
                if pos == self.size_of_the_board:
                    winner = 1
                    print(f"{player} is the winner")
                    break
        df = pd.DataFrame(self.move_history)
        summary = (
            df.groupby("Players")
            .agg({
                "Dice Roll History": lambda x: ", ".join(map(str, x)),
                "Postion History": lambda x: ", ".join(map(str, x)),
                "Win Status": "last"
            })
            .reset_index()
        )
        return summary
                    
            

game = SnakeAndLadder()
print(game.play())
        