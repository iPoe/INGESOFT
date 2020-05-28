from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import smtplib


def send_email(email,username,password):
    message = 'Bienvenido a Nutristory App!!\n\nUsuario: {}\n\n Contrasenia: {}'.format(username,password)
    subject = 'Informacion Cuenta Nutristory App'
    message = 'Subject: {}\n\n{}'.format(subject,message)
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('nutristoryapp@gmail.com','nutri12345')
    server.sendmail('nutristoryapp@gmail.com',email,message)
    server.quit()

def add_nutritionist(mysql,idNut,name,docType,phone,email,username,password):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    # Check if account exists using MySQL
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('INSERT INTO nutricionista (idNutricionista,nombre,usuario,pass,tipoDoc,telefono,email) VALUES (%s,%s,%s,%s,%s,%s,%s)',(idNut,name,username,password,docType,phone,email))
    mysql.connection.commit()
    send_email(email,username,password)
    msg = "Nutricionista Creado Con Exito!"
    return msg

def search_nutritionist(mysql,username):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM nutricionista WHERE idNutricionista = %s', [username])
    # Fetch one record and return result
    return cursor.fetchone()
