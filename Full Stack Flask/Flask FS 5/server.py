from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

users = []
posts = []
@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if any(u['username'] == username for u in users):
            error = "Username already exists."
        else:
            users.append({'username': username, 'password': password})
            session['username'] = username
            return redirect(url_for('feed'))
    return render_template('register.html', error=error)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = next((u for u in users if u['username'] == username and u['password'] == password), None)
        if user:
            session['username'] = username
            return redirect(url_for('feed'))
        else:
            error = "Invalid credentials."
    return render_template('login.html', error=error)
@app.route('/feed', methods=['GET', 'POST'])
def feed():
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        content = request.form['content']
        posts.append({'author': session['username'], 'content': content})
    return render_template('feed.html', username=session['username'], posts=posts)
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)