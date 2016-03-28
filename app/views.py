from flask import render_template

from app import app


@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/sign_up')
def show_sign_up():
    return render_template('signup.html')
