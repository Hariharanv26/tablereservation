from app import app 

from flask import render_template, make_response


@app.route('/')
def index():
    return make_response(render_template('public/home.html'))