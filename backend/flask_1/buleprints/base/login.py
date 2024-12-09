from urllib import request

from flask import Blueprint

bp = Blueprint('login', __name__, url_prefix='/login')

@bp.route("/",methods=['GET','POST'])
def index():
    if request.method == "GET":
        return "get"
    elif request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        return username,password

