from flask import render_template, make_response
from . import viewsBP as viewAPI

@viewAPI.route('/')
def index():
    return make_response(render_template('index.html'), 200)
