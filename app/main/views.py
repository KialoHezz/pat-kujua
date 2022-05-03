from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources


@main.route('/')
def home_page():
    title = "News Page"

    return render_template('homepage.html', title =title)
