from flask import Blueprint, render_template, redirect, url_for,request,flash
from flask_login import login_user,logout_user,login_required,current_user
from werkzeug.security  import generate_password_hash,check_password_hash
from . import db,mail
from .models import user_table
import re
from flask_mail import Mail,Message

auth = Blueprint('auth',__name__)


def check_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False

def password_mismatch(password1,password2):
    if password1 != password2:
        return "passwords not matching"
    elif  len(password1)<5:
        return "passwords should be minimum 6 characters long"
    else:
        return False

def check_valid(email_exists,user_exists,email,password1,password2,username):
    if email_exists:
        flash("Email already in use",category="error")
        return 0
    elif user_exists:
        flash("Username already in use",category="error")
        return 0
    elif password_mismatch(password1,password2):
        flash(f"{password_mismatch(password1, password2)}",category="error")
        return 0
    elif len(username)<2:
        flash("Username should have minimum 2 characters ",category="error")
        return 0
    elif not check_email(email):
        flash("Not a valid email")
        return 0    
    else: 
        return 1


def create_user():
    username = request.form.get("username")
    email = request.form.get("email")
    password1 = request.form.get("password1")
    password2 = request.form.get("password2")
    email_exists = user_table.query.filter_by(email = email).first()
    user_exists = user_table.query.filter_by(username = username).first()

    if check_valid(email_exists,user_exists,email,password1,password2,username):    
        new_user = user_table(username = username, email = email, password = generate_password_hash(password1, method = "sha256"))
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user,remember = True)
        flash('User Created')
        return redirect(url_for("views.home"))
    else:
        return render_template("signup.html",user = current_user)





@auth.route('/signup', methods = ["GET","POST"])
def signup(): 
    if request.method =="POST":
       return create_user()
    return render_template("signup.html",user = current_user)




@auth.route('/login',methods = ["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = user_table.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("logging in",category="success")
                login_user(user, remember= True)
                return redirect(url_for("views.index"))
            else:
                flash("Password is incorrect",category="error")

        else:
            flash("Email does not exist")    

    return render_template("login.html", user = current_user)


@auth.route('/logout')
@login_required
def logout():
   logout_user()
   return  redirect(url_for("views.home"))

def send_email(user):
    token = user.get_reset_token()
    msg =  Message('Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
        {url_for('auth.reset_token', token=token,_external=True)}
        If you did not make this request then simply ignore this email and no changes will be made.
    '''
    mail.send(msg)

@auth.route('/reset_request.html', methods = ["GET", "POST"])
def reset_request():
    if request.method == "POST":
        email = request.form.get("email")
        user = user_table.query.filter_by(email = email).first()
        if user:
            send_email(user)
            flash('Password reset link sent to email')
            return redirect(url_for('auth.login'))
        else:
            flash('Email does not exist')
    return render_template('reset_request.html',user = current_user)



@auth.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if token != "{url_for('auth.reset_password')}":
        user = user_table.verify_reset_token(token)
        if user is None:
            flash('That is an invalid or expired token', 'warning')
            return redirect(url_for('auth.reset_request'))

    if request.method == "POST":
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        user_id = request.form.get("user")
        user = db.session.query(user_table).get(user_id)
        if not password_mismatch(password,confirm_password):
            hashed_password = generate_password_hash(password,method = "sha256")
            user.password = hashed_password
            db.session.commit()
            flash('Your password has been updated! You are now able to log in', 'success')
            return redirect(url_for('auth.login'))
        else:
            flash(f"{password_mismatch(password,confirm_password)}")
    return render_template('reset_token.html',user=user)