# Se importan las librerias
from random import randint
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL

import MySQLdb.cursors
import re
from App.data import *

application = Flask(__name__)

# Change this to your secret key (can be anything, it's for extra protection)
application.secret_key = 'your secret key'

# Enter your database connection details below
application.config['MYSQL_HOST'] = 'nutry-app.ckkbcotpyks6.us-east-1.rds.amazonaws.com'
application.config['MYSQL_USER'] = 'admin1'
application.config['MYSQL_PASSWORD'] = 'Monster14320'
application.config['MYSQL_PORT'] = 3306
application.config['MYSQL_DB'] = 'DB_APP'

mysql = MySQL(application)
from App.decorators import *
from App.nutritionist.routes import mod
from App.admin.routes import mod

application.register_blueprint(nutritionist.routes.mod)
application.register_blueprint(admin.routes.mod)

# http://localhost:5000/login/ - this will be the login page, we need to use both GET and POST requests
@application.route('/login/', methods=['GET', 'POST'])
@not_login_required
def login():
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST':
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        #check admin
        if username == "admin" and password == "12345":
            session['loggedin'] = True
            session['id'] = "-1"
            session['username'] = username
            session['search'] = "False"
            return redirect(url_for('admin.homeAdmin'))
        else:
            account = search_user(mysql,username,password)
             # If account exists in accounts table in out database
            if account:
                # Create session data, we can access this data in other routes
                session['loggedin'] = True
                session['id'] = account['idNutricionista']
                session['username'] = account['nombre']
                session['search'] = "False"
                # Redirect to home page
                return redirect(url_for('nutritionist.home'))
            else:
                # Account doesnt exist or username/password incorrect
                msg = 'Usuario o Contraseña incorrectos!'

    return render_template('index.html', msg=msg)

# http://localhost:5000/login/logout - this will be the logout page
@application.route('/logout')
@login_required
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   session.pop('search', None)
   # Redirect to login page
   return redirect(url_for('login'))
