from flask import render_template
from . import main
from ..requests import get_sources


@main.route('/')
def home_page():
    title = "News Page"

    return render_template('homepage.html', title =title)