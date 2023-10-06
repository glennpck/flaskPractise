from flask import render_template, url_for, flash, redirect
from HelloWorld.forms import RegistrationForm, LoginForm
from HelloWorld.models import User, Post
from HelloWorld import app, db, bcrypt

posts = [
    {
        'author': 'Nnelg Hep',
        'title': 'Post 1',
        'content': 'Testing it out',
        'date_posted': '4 September, 2023'
    },
    {
        'author': 'Trebled Pay',
        'title': 'Post 2',
        'content': 'Testing it out again',
        'date_posted': '4 September, 2023'
    },
]

@app.route("/")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='nagger!')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():

        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, 
                    email=form.email.data, 
                    password=hashed_pw)
        
        db.session.add(user)
        db.session.commit()

        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            return redirect(url_for('home'))
        
        else:

            flash('Login in Unsuccessful. Please check email and pass', 'danger')
            
    return render_template('login.html', title='Login', form=form)