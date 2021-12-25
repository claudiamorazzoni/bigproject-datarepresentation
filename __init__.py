from flask import Flask, url_for, render_template, request, redirect, url_for, flash, session, jsonify, abort, make_response, redirect, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
import mysql.connector
from mysql.connector import cursor
import dbconfig as cfg

#Create the Flask app
app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Mcm_290576'
app.config['MYSQL_DB'] = 'crud'

mysql = MySQL(app)


# First route
@app.route('/')
def root():
    if not 'username' in session:
        return redirect(url_for('login'))


# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT username,password FROM users WHERE username=%s", [username])
        user = cur.fetchone()
        if user:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['username'] = user['username']
            return render_template('index2.html', username=username)
        
        else:
            flash('Invalid Username or Password !!')
            return render_template('login.html')
    else:
        return render_template('login.html')


# Logout
@app.route('/logout')
def logout():
    session.clear()
    return render_template('login.html')

# /home route renders home template
@app.route('/index')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM students")
    data = cur.fetchall()
    cur.close()
    
    return render_template('index2.html', students=data )


# the students records being created 
@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        flash("Data Inserted Successfully")
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO students (name, email, phone) VALUES (%s, %s, %s)", (name, email, phone))
        mysql.connection.commit()
        return redirect(url_for('index'))


# the students records being deleted
@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM students WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('index'))


# the students records being updated
@app.route('/update',methods=['POST','GET'])
def update():

    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE students
               SET name=%s, email=%s, phone=%s
               WHERE id=%s
            """, (name, email, phone, id_data))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('index'))

#Run Flask
if __name__ == "__main__":
    app.run(debug=True)