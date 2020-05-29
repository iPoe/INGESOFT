from functools import wraps

from flask import abort,render_template,redirect, url_for, session

def not_login_required(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        #verifica si ya está logeado, en caso de estarlo hace lo devuelve a home
        if 'loggedin' in session:
            if session['id'] == "-1":
                # User is loggedin show them the home page
                return redirect(url_for('admin.homeAdmin'))
            else:
                return redirect(url_for('nutritionist.home'))
        # Output message if something goes wrong...
        return f(*args, **kws)
    return decorated_function

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        #verifica si ya está logeado, en caso de estarlo hace lo devuelve a home
        if not 'loggedin' in session:
            return redirect(url_for('login'))
        return f(*args, **kws)
    return decorated_function

def nutritionist_required(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        if session['id'] == "-1":
            abort(401)
        return f(*args, **kws)
    return decorated_function


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        if session['id'] != "-1":
            abort(401)
        return f(*args, **kws)
    return decorated_function

def search_required(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        if session['search'] == "False":
            abort(401)
        return f(*args, **kws)
    return decorated_function
