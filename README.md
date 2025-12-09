# SnakeAndLadder

A simple Python implementation of the classic **Snake and Ladder** board game with a small twist without snakes and ladder.  
This version includes four players and tracks every move until a winner is declared.

## Features
- Four players: `player1`, `player2`, `player3`, `player4`
- Random dice rolls
- Validates board limits
- Tracks full move history
- Generates a summary of dice rolls, positions, and win status
- Uses **pandas** for data output

## How to Run
```bash
python SnakeAndLadder.py
```

# SnakeAndLadder Part- B

Its an extension of the previous version of snakeandladder here I have added the cut logic and linear position is converted as coordinates (rows,columns).

1. Player Cut Logic
  - If a player lands on a tile where another player is standing the other player is cut and sent back to position 0 which marked (-1, -1) in co-ordinates.

2. Linear Position → 2D Coordinate Conversion
  - Convert to 0-based index
  - Compute (row, col) using divmod()
  - Reverse col for odd-numbered rows
  - Store the result in move history

## How to Run
```bash
python SnakeAndLadderPartB.py
```
