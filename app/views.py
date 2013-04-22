from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Person' } # fake user
    posts = [ # fake array of posts
    	{ 
            'author': { 'nickname': 'John' }, 
            'body': 'Beautiful day in Portlandia!' 
        },
        { 
            'author': { 'nickname': 'Susan' }, 
            'body': 'The Avengers movie was so cool!' 
        },
        { 
            'author': { 'nickname': 'roshow' }, 
            'body': 'Why so serious?' 
        },
        { 
            'author': { 'nickname': 'Shawn' }, 
            'body': 'I heard it both ways.' 
        }
    ]
    return render_template("index.html", title = 'Shiznit', user = user, posts = posts)	

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', 
        title = 'Sign In',
        form = form)