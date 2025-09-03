from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = [
    {"id": 1, "first_name": "Jimmy", "last_name": "Jun", "email": "jjun@gmail.com", "created_at": "June 15th, 2015"},
    {"id": 2, "first_name": "Andrew", "last_name": "Lee", "email": "alee@gmail.com", "created_at": "June 16th, 2015"},
    {"id": 3, "first_name": "Jay", "last_name": "Patel", "email": "jpatel@gmail.com", "created_at": "June 17th, 2015"},
    {"id": 4, "first_name": "Eduardo", "last_name": "Baik", "email": "ebaik@gmail.com", "created_at": "June 18th, 2015"}
]

@app.route('/users')
def users_index():
    return render_template('users_index.html', users=users)

@app.route('/users/<int:user_id>')
def user_show(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return "User not found", 404
    return render_template('user_show.html', user=user)

@app.route('/users/new')
def user_new():
    return render_template('users_new.html')

@app.route('/users/create', methods=['POST'])
def user_create():
    new_id = max(u["id"] for u in users) + 1 if users else 1
    user = {
        "id": new_id,
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "created_at": request.form.get('created_at', 'Today')
    }
    users.append(user)
    return redirect(url_for('users_index'))

@app.route('/users/<int:user_id>/edit')
def user_edit(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return "User not found", 404
    return render_template('user_edit.html', user=user)

@app.route('/users/<int:user_id>/update', methods=['POST'])
def user_update(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return "User not found", 404
    user["first_name"] = request.form['first_name']
    user["last_name"] = request.form['last_name']
    user["email"] = request.form['email']
    return redirect(url_for('users_index'))

@app.route('/users/<int:user_id>/destroy', methods=['POST'])
def user_destroy(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return redirect(url_for('users_index'))

if __name__ == "__main__":
    app.run(debug=True)    # ...existing code...
    