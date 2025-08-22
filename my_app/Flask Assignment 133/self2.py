from flask import Flask, render_template


app = Flask(__name__)

@app.route('/home')
def home():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return render_template("loop.html", numbers=numbers)

@app.route('/about')
def about():
    return render_template("self2.html")

if __name__ == "__main__":
    app.run(debug=True)