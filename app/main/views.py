from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources

@main.route('/')
def index():
    id = get_sources('id')
    name = get_sources('name')
    urlToImage = get_sources('urlToImage')
    description = get_sources('description')
    publishedAt = get_sources('publishedAt')

    return render_template('index.html',id=id, name=name,urlToImage=urlToImage,description=description,publishedAt=publishedAt)

@main.route('/')
def home_page():
    title = "News Page"

    return render_template('homepage.html', title =title)
