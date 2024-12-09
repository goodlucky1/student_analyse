from urllib import request

from flask import Blueprint

bp = Blueprint('registry', __name__, url_prefix='/registry')

@bp.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'GET':
        return ""
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        return username + password + email