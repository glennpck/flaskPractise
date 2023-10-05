from flask import render_template, url_for, flash, redirect
from HelloWorld.forms import RegistrationForm, LoginForm
from HelloWorld.models import User, Post
from HelloWorld import app

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
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == "password":
            flash(f'Log in successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login in Unsuccessful. Please check email and pass', 'danger')
            
    return render_template('login.html', title='Login', form=form)