import random
import pandas as pd

class SnakeAndLadder:
    def __init__(self):
        self.players = [f"player{i+1}"for i in range(4)]
        self.size_of_the_board = 16
        self.players_position = {player:0 for player in self.players}
        self.move_history = []
    

    def roll_dice(self):
        return random.randint(1,6)
    
    def move_player(self, player, dice):
        new_position = self.players_position[player] + dice
        if new_position > self.size_of_the_board:
            print(f"{player} cannot move beyond the board size")
            return self.players_position[player]
        print(f"{player} moves from {self.players_position[player]} to {new_position}")
        self.players_position[player] = new_position
        return new_position

    def cut_player(self, pos, player):
        for old_player in self.players_position.keys():
            if old_player != player and pos != 0 and self.players_position[old_player] == pos:
                self.players_position[old_player] = 0

                self.move_history.append({
                    "Players": old_player,
                    "Dice Roll History": 0,
                    "Postion History": 0,
                    "2d coordinates": (-1, -1),  #since player moved to default position
                    "Win Status": 0
                })

    def pos_to_2d(self, pos):
        # index starts at 0 not 1 i.e., for position 16 it would (0,3)
        pos = pos-1
        co_ord =  divmod(pos, 4)
        if co_ord[0]%2 != 0:
            actual_co_ord = (co_ord[0], 4-co_ord[1]-1)
            return actual_co_ord 
        return co_ord  
    
    def play(self):
        print("starting the game")
        winner = 0 
        while not winner:
            for player in self.players:
                dice = self.roll_dice()
                pos = self.move_player(player,dice)
                self.cut_player(pos, player)
                co_ord = self.pos_to_2d(pos)
                self.move_history.append({
                    "Players": player,
                    "Dice Roll History": dice,
                    "Postion History": pos,
                    "2d coordinates": co_ord,
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
                "2d coordinates": lambda x: ", ".join(map(str, x)),
                "Win Status": "last"
            })
            .reset_index()
        )
        return summary
                    
            

game = SnakeAndLadder()
print(game.play())