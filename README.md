# 🎮 Flask Mini Games hub

This is a Flask-based web application featuring three interactive components:

1. 🤖 **Tic Tac Toe** – Play against an AI opponent.
2. 🧩 **Sudoku Solver** – Input a Sudoku puzzle and get an instant solution.
3. 🔢 **Number Guesser** – Try to guess a random number with hints after each guess.

---

## 🚀 Features

- **Tic Tac Toe AI**
  - Smart AI opponent using custom move logic.
  - Returns the AI move and checks for winners via JSON API.

- **Sudoku Solver**
  - Accepts 9x9 puzzles via JSON.
  - Uses a backtracking algorithm to solve.

- **Number Guesser Game**
  - Random number between 1–100 generated per session.
  - Binary search-style hints guide the player.
  - Resets after a correct guess.

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/shashwatMittel/flask-mini-games.git
cd flask-mini-games
