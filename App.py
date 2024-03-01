from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    secret_number = random.randint(1, 100)
    attempts = 0
    message = ''



    while True:
        guess = int(request.form['guess'])
        attempts += 1

        if guess < secret_number:
            message = "Too low! Try again."
        elif guess > secret_number:
            message = "Too high! Try again."
        else:
            message = f"Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts."
            break

    return render_template('result.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
