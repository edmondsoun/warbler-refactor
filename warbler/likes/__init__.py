from flask import Blueprint

likes = Blueprint('likes',
                 __name__,
                 template_folder='templates',
                 static_folder='static')

from . import views