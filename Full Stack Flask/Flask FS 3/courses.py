from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

courses = [
    {"id": 1, "name": "How to be a ninja", "description": "Learn ninja skills", "date_added": "Dec 1st 2013 5:34PM"},
    {"id": 2, "name": "How to fly", "description": "Learn to fly", "date_added": "Nov 1st 2011 11:12AM"},
    {"id": 3, "name": "How to get more energy in the bootcamp", "description": "Description about this course...", "date_added": "Oct 1st 2013 11:11AM"},
    {"id": 4, "name": "How to pair program more effectively", "description": "Pair programming tips", "date_added": "Sep 28th 2011 10:15PM"}
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        date_added = datetime.now().strftime("%b %d %Y %I:%M%p")
        new_id = max(course["id"] for course in courses) + 1 if courses else 1
        courses.append({"id": new_id, "name": name, "description": description, "date_added": date_added})
        return redirect(url_for('index'))
    return render_template('courses.html', courses=courses)

@app.route('/courses/destroy/<int:course_id>')
def destroy_course(course_id):
    course = next((c for c in courses if c["id"] == course_id), None)
    if not course:
        return "Course not found", 404
    return render_template('delete_course.html', course=course, course_id=course_id)

@app.route('/courses/delete/<int:course_id>', methods=['POST'])
def delete_course(course_id):
    global courses
    courses = [c for c in courses if c["id"] != course_id]
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)