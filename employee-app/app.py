from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    major = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Student {self.name}>"

# Initialize the database (create tables)
with app.app_context():
    db.create_all()

# Home route (Read)
@app.route('/')
def home():
    students = Student.query.all()
    return render_template('read.html', students=students)

# Create route
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        major = request.form['major']
        new_student = Student(name=name, age=age, major=major)
        db.session.add(new_student)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('create.html')

# Update route
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    student = Student.query.get_or_404(id)
    if request.method == 'POST':
        student.name = request.form['name']
        student.age = request.form['age']
        student.major = request.form['major']
        db.session.commit()
        return redirect(url_for('home'))
    
    return render_template('update.html', student=student)

# Delete route
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    student = Student.query.get_or_404(id)
    if request.method == 'POST':
        db.session.delete(student)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('delete.html', id=id)

if __name__ == '__main__':
    app.run(debug=True)
