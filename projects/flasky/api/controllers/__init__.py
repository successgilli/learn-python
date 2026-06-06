from flask import Blueprint

viewsBP = Blueprint('views', __name__, url_prefix='/api/v1')

from . import views, errors
