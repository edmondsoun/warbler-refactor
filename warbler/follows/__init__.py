from flask import Blueprint

follows = Blueprint('follows',
                 __name__,
                 template_folder='templates',
                 static_folder='static')

from . import views