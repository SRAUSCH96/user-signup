from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/index')
def index_display():
    return render_template('index.html', title='Signup')



@app.route('/index', methods=['POST'])
def index_signup():
    username = request.form['username']
    password = request.form['user_password']
    verify_password = request.form['verify_password']
    email = request.form['user_email']
    space = " "
    email1 = "@"
    email2 = "."
    username_error = ""
    password_error = ""
    verify_password_error = ""
    email_error = ""

    if space in username:
        username_error = 'Cannot contain spaces'
        username = ""
    if len(username) < 3 or len(username) > 20:
        username_error = 'Invalid Username'
        username = ""
    if space in password:
        password_error = 'Cannot contain spaces'
        password = ""
    if len(password) < 3 or len(password) > 20:
        password_error = 'Invalid password'
        password = ""
    if verify_password not in password:
         verify_password_error = 'Passwords do not match'
         verify_password = ""
    if len(email) > 0:
        if not len(email) > 3 and len(email) < 20:
            email_error = "Invalid Email"
            email = ""
        if email1 and email2 not in email:
            email_error = "Invalid Email"
            email = ""

    
    if not username_error and not password_error and not verify_password_error and not email_error:
        return redirect("/Welcome?username={0}".format(username))
    else:
        return render_template("index.html", username = username, user_email = email, username_error = username_error, password_error = password_error, verify_password_error = verify_password_error, email_error = email_error, title= "Signup")
@app.route("/Welcome")
def welcome():
    user = request.args.get('username')
    return render_template('welcome.html', user=user )

app.run()