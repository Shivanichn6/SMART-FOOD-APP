from flask import session, redirect, url_for

def check_login():

    if 'user' not in session:

        return redirect(url_for('signin'))

    return None