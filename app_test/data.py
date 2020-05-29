from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

def search_user(mysql,username,password):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM nutricionista WHERE usuario = %s AND pass = %s', (username, password))
    # Fetch one record and return result
    return cursor.fetchone()
