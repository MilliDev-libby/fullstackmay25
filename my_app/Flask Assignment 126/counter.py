from flask import Flask, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
    else:
        session['counter'] += 1
    return f"Counter: {session['counter']}"

@app.route('/addtwo')
def add_two():
    if 'counter' not in session:
        session['counter'] = 0
    session['counter'] += 2
    return f"Counter: {session['counter']}"

@app.route('/reset')
def reset():
    session['counter'] = 0
    return f"Counter reset! Counter: {session['counter']}"

if __name__ == "__main__":
    app.run(debug=True)