# 🎮 Tic Tac Toe: Recurse Center Interview Challenge 🎲💻

---

```python
# board = [{0:0,1:0,2:1},{0:1,1:1,2:3},{0:1,1:1,2:3}]

size = int(input('How large do you want the board?'))
...
# rest of the code
...
draw(board)
checkwin(board)
```
---

## 📚 Introduction 📚

Welcome to our interactive implementation of the classic game: Tic Tac Toe. This project was built as a coding challenge for the interview process at Recurse Center. It features a dynamic game board size, and player turns with winning condition checks. 

### 🎲 The Game 🎲

Tic Tac Toe, or Noughts and Crosses, is a classic game typically played on a grid of 3x3. The goal is to place three of your marks (either 'X' or 'O') in a horizontal, vertical, or diagonal row before your opponent does. In our version, you can define your own board size to increase the complexity of the game. How exciting!

```python
size = int(input('How large do you want the board?'))
```

### 🔄 Player Turns & Winning Conditions 🔄

After setting up the game board, the game proceeds by taking turns between the players. Each player gets to place their mark ('X' or 'O') in an unoccupied cell. 

Once a player has made their move, the game will check for a win condition, which is defined as having a full row, column, or diagonal filled with a player's mark. The game ends when a player meets the winning conditions or when all cells are filled and no player has won.

### 🎨 The `draw` Function & `checkwin` Function 🎨

The `draw` function is responsible for rendering the game board after every move. The `checkwin` function is responsible for determining whether a player has won the game or not.

```python
draw(board)
checkwin(board)
```

---

## 🌐 External Resources 🌐

- Python Official Documentation: https://docs.python.org/3/
- Tic Tac Toe Game Rules: https://www.exploratorium.edu/brain_explorer/tictactoe.html
- Recurse Center: https://www.recurse.com/

---

## 😅 Conclusion 😅

This Tic Tac Toe project was an exciting challenge proposed by Recurse Center that allowed us to dive deeper into Python coding and game logic implementation. Feel free to try it out, adapt it, or even expand on it. Enjoy playing, and may the best player win! 🎲🚀💻🎉
