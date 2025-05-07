from flask import Flask, render_template, request, jsonify, session
from tictactoe import get_ai_move, check_winner
from sudoku_solver import solve_sudoku
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tictactoe/move', methods=['POST'])
def tictactoe_move():
    data = request.json
    board = data['board']
    ai_move = get_ai_move(board)
    winner = check_winner(board)
    return jsonify({'ai_move': ai_move, 'winner': winner})

@app.route('/sudoku/solve', methods=['POST'])
def sudoku():
    data = request.json
    board = data['board']
    solution = solve_sudoku(board)
    return jsonify({'solution': solution})

# === Number Guesser Game ===
@app.route('/number_guesser', methods=['GET', 'POST'])
def number_guesser():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
        session['min'] = 1
        session['max'] = 100
        session['attempts'] = 0

    hint = ""
    if request.method == 'POST':
        guess = int(request.form['guess'])
        session['attempts'] += 1
        number = session['number']

        # AI Feedback Hint using Binary Search Principle
        if guess < number:
            session['min'] = max(session['min'], guess + 1)
            hint = "Too low! Try a number between {} and {}".format(session['min'], session['max'])
        elif guess > number:
            session['max'] = min(session['max'], guess - 1)
            hint = "Too high! Try a number between {} and {}".format(session['min'], session['max'])
        else:
            hint = f"🎉 Correct! The number was {number}. Attempts: {session['attempts']}"
            session.clear()

    return render_template('number_guesser.html', hint=hint)

if __name__ == '__main__':
    app.run(debug=True)
