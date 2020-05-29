# Se importan las librerias
from random import randint
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from flask import Blueprint
from app_test import mysql
from app_test.decorators import *

mod = Blueprint('nutritionist',__name__)

# http://localhost:5000/pythinlogin/home - this will be the home page, only accessible for loggedin users
@mod.route('/home')
@login_required
@nutritionist_required
def home():
    session['search'] = "False"
    return render_template('home.html', username=session['username'])
