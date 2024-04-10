from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'registration_db'

mysql = MySQL(app)

# Root endpoint - renders registration form
@app.route('/')
def registration_form():
    return render_template('register.html')

# Register endpoint - handles form submission
@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        # Fetch form data
        student_name = request.form['student_name']
        father_name = request.form['father_name']
        mother_name = request.form['mother_name']
        phone_number = request.form['phone_number']
        email = request.form['email']
        date_of_birth = request.form['date_of_birth']
        address = request.form['address']
        blood_group = request.form['blood_group']
        department = request.form['department']
        course = request.form['course']
        password = request.form['password']

        # Hash the password before storing it
        hashed_password = generate_password_hash(password)

        # Store data in the database
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (student_name, father_name, mother_name, phone_number, email, date_of_birth, address, blood_group, department, course, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (student_name, father_name, mother_name, phone_number, email, date_of_birth, address, blood_group, department, course, hashed_password))
        mysql.connection.commit()
        cur.close()

        return redirect(url_for('registration_form'))

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
