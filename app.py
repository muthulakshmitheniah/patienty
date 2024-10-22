

from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = 'abc@123'

# Database initialization and table creation
def init_db():
    with sqlite3.connect('DATA.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS webmedconsultmaster (
                sno INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                phone INTEGER NOT NULL,
                email TEXT NOT NULL,
                Age INTEGER NOT NULL,
                gender TEXT NOT NULL,
                height INTEGER NOT NULL,
                Weight INTEGER NOT NULL,
                bloodgroup TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Appoinment (
                sno INTEGER PRIMARY KEY,
                appoinmentname TEXT NOT NULL,
                email TEXT NOT NULL,
                doctor TEXT NOT NULL,             
                message TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Contact (
                sno INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                message TEXT NOT NULL
            )
        ''')
        connection.commit()

init_db()  # Initialize the database on application start

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        with sqlite3.connect('DATA.db') as connection:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO Contact (name, email, message) VALUES (?, ?, ?);', (name, email, message))
            connection.commit()
    return render_template('return3.html')

@app.route('/form', methods=["GET", "POST"])
def form():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        Age = request.form['Age']
        gender = request.form['gender']
        height = request.form['height']
        Weight = request.form['Weight']
        bloodgroup = request.form['bloodgroup']

        with sqlite3.connect('DATA.db') as connection:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO webmedconsultmaster (name, phone, email, Age, gender, height, Weight, bloodgroup) VALUES (?, ?, ?, ?, ?, ?, ?, ?);',
                           (name, phone, email, Age, gender, height, Weight, bloodgroup))
            connection.commit()
        return render_template('return.html')

    return render_template('form.html')


@app.route('/login')
def login():
    # return 'Hello, World!'
    # if request.method == "POST":
        

    return render_template('login.html')


@app.route('/videocall')
def videocall():
    # return 'Hello, World!'
    return render_template('videocall.html')

@app.route('/doctinfo1')
def doctinfo1():
    # return 'Hello, World!'
    return render_template('doctinfo1.html')

@app.route('/doctinfo2')
def doctinfo2():
    # return 'Hello, World!'
    return render_template('doctinfo2.html')

@app.route('/doctinfo3')
def doctinfo3():
    # return 'Hello, World!'
    return render_template('doctinfo3.html')

@app.route('/docs')
def docs():
    # return 'Hello, World!'
    return render_template('docs.html')

@app.route('/gmeet')
def gmeet():
    # return 'Hello, World!'
    return render_template('gmeet.html')

@app.route('/appoinment', methods=["GET", "POST"])
def appoinment():
    if request.method == 'POST':
        appoinmentname = request.form['appoinmentname']
        email = request.form['email']
        doctor = request.form['doctor']
        message = request.form['message']

        with sqlite3.connect('DATA.db') as connection:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO Appoinment (appoinmentname, email, doctor, message) VALUES (?, ?, ?, ?);',
                           (appoinmentname, email, doctor,  message))
            connection.commit()

        return render_template('return2.html')

    return render_template('appoinment.html')

if __name__ =="__main__":
    app.run(debug=True)