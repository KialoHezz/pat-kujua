from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_articles

@main.route('/')
def index():
    source = get_sources()
    # articles = get_articles()
    
    return render_template('index.html',source=source)



@main.route('/')
def home_page():
    title = "News Page"

    return render_template('homepage.html', title =title)
