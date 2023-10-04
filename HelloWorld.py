from flask import Flask, render_template

app = Flask(__name__)

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
