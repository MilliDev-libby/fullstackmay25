from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    username = db.Column(db.String(50))
    email = db.Column(db.String(120))
    password = db.Column(db.String(120))

# Create the database
with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user = User(
            first_name=request.form['first_name'],
            last_name=request.form['last_name'],
            username=request.form['username'],
            email=request.form['email'],
            password=request.form['password']
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('display', user_id=user.id))
    return render_template('form.html')

@app.route('/display/<int:user_id>')
def display(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('display.html', user=user)

if __name__ == "__main__":
    app.run(debug=True)