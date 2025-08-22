from flask import Flask, render_template,request


app = Flask(__name__)

@app.route('/')
def test():
    return render_template("index.html", test = "Test")

@app.route('/contact', methods = ["GET", "POST"] )
def contact():
    name = request.form['first_name'] + request.form['last_name']
    email = request.form['email']
    address = request.form['address']
    city = request.form['city']
    state = request.form['state']
    zipcode = request.form['zip']
    return render_template("contact.html", name=name, email=email, address=address, city=city, state=state, zipcode=zipcode)

if __name__ == "__main__":
    app.run(debug=True)