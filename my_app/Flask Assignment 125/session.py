from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def test():
    return render_template("index.html", test="Test")

@app.route('/formdata', methods=["POST", "GET"])
def formdata():
    if request.method == "POST":
        session['name'] = request.form['first_name'] + " " + request.form['last_name']
        session['email'] = request.form['email']
        session['address'] = request.form['address']
        session['city'] = request.form['city']
        session['state'] = request.form['state']
        session['zipcode'] = request.form['zip']
    return render_template(
        "formdata.html",
        name=session.get('name', ''),
        email=session.get('email', ''),
        address=session.get('address', ''),
        city=session.get('city', ''),
        state=session.get('state', ''),
        zipcode=session.get('zipcode', '')
    )

if __name__ == "__main__":
    app.run(debug=True)