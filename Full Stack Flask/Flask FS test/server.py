from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

appointments = []

@app.route('/')
def index():
    return render_template('appointments.html', appointments=appointments)

@app.route('/new_appointment', methods=['GET', 'POST'])
def new_appointment():
    if request.method == 'POST':
        date = request.form['date']
        time = request.form['time']
        patient = request.form['patient']
        complaint = request.form['complaint']
        appointments.append({
            'date': date,
            'time': time,
            'patient': patient,
            'complaint': complaint
        })
        return redirect(url_for('index'))
    return render_template('new_appointments.html')

@app.route('/cancel_all', methods=['POST'])
def cancel_all():
    appointments.clear()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)