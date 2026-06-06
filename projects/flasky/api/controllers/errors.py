from flask import make_response, render_template
from . import viewsBP as viewAPI

@viewAPI.app_errorhandler(404)
def handle_404(e):
    return make_response(render_template('404.html'), 404)
