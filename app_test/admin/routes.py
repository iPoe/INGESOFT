
# Se importan las librerias
from random import randint
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from flask import Blueprint
from app_test import mysql
from app_test.admin.data import *
from app_test.decorators import *

mod = Blueprint('admin',__name__)

@mod.route('/homeAdmin')
@login_required
@admin_required
def homeAdmin():
    session['search'] = "False"
    return render_template('homeAdmin.html', username=session['username'])


@mod.route('/newNut/',methods=['GET', 'POST'])
@login_required
@admin_required
def newNut():
    session['search'] = "False"
    msg = ''
    if request.method == 'POST':
        # Create variables for easy access
        name = request.form['name']
        idNut = request.form['idNut']
        docType = request.form['docType']
        phone = request.form['phone']
        email = request.form['email']
        username = request.form['idNut']
        password = str(randint(10000,99999))

        msg = add_nutritionist(mysql,idNut,name,docType,phone,email,username,password)
        flash(msg)
        return redirect(url_for('admin.homeAdmin'))
    return render_template('newNut.html')

@mod.route('/search_nut/',methods=['GET', 'POST'])
@login_required
@admin_required
def search_nut():
    session['search'] = "False"
    msg = ''
    if request.method == 'POST':
        # Create variables for easy access
        idNut = request.form['idNut']
        exist = search_nutritionist(mysql,idNut)
        if exist:
            session['search'] = idNut
            return redirect(url_for('admin.select'))
        else:
            msg = 'No Existe Un Nutricionista asociado a ese número de identificación'
    return render_template('search_nut.html', msg=msg)



@mod.route('/select/')
@login_required
@admin_required
@search_required
def select():
    return render_template('select.html')
