"""
Web server backend for Muse2pokecrystal.

The server depends on flask and is a kind of a wrapper
around the command line interface for the most part.
"""

from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
SERV = Flask(__name__)
Bootstrap(SERV)


@SERV.route('/')
def main_page():
    return render_template('index.html.jinja')
