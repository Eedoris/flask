from flask import Blueprint,render_template,url_for,request,redirect,flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user,logout_user, login_required
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login',methods=['POST', 'GET'])
def login():
  if request.method == 'GET':
    return render_template('login.html')
  else:
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
      return redirect(url_for('auth.login')) 
    
    login_user(user, remember=remember)

    return redirect(url_for('main.profile'))
   

@auth.route('/signup',methods=['POST', 'GET'])
def signup():
    if request.method == 'GET':
      return render_template('signup.html')
    
    else:
      email = request.form.get('email')
      name = request.form.get('name')
      password = request.form.get('password')
      confirmPassword = request.form.get('confirmPassword')

      user = User.query.filter_by(email=email).first() 

      if user: 
        return redirect(url_for('auth.signup'))
      
      elif password != confirmPassword: 
        return redirect(url_for('auth.signup'))
      
      elif len(password) < 4 :
        return redirect(url_for('auth.signup'))
      
      else:
        new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()

        
        return redirect(url_for('auth.login'))

    

@auth.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('main.index'))
