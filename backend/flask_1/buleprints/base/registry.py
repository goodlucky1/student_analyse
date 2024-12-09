from flask import Blueprint,request,session
from wtforms import Form, StringField, IntegerField, validators,EmailField
from wtforms.validators import ValidationError
from flask import Blueprint
from flask_model import model
from flask_dbobject.dbobject import db

bp = Blueprint('registry', __name__, url_prefix='/registry')

class RegistryForm(Form):
    username=StringField("username", validators=[validators.Length(min=3, max=100, message="this length is 3 to 100"),validators.DataRequired("this is required")])
    password=StringField("password", validators=[validators.Length(min=6, max=100, message="this length is 6 to 100"),validators.DataRequired(message="this is required")])
    email=StringField("email", validators=[validators.email(message="use email format"),validators.DataRequired("this is not required")])
    def validate_username(self,filed):
        user= model.User.query.filter_by(username=filed.data).first()
        if user is not None:
            raise ValidationError("该用户已被注册")




@bp.route('/', methods=('GET', 'POST'))
def index():
    if request.method == "GET":
        return {"result":"success"}
    elif request.method == "POST":
        re = RegistryForm(request.args)
        if re.validate():
            user = model.User(username=request.args.get("username"), password=request.args.get("password"),
                              email=request.args.get("email"), userRole=request.args.get("userRole"))
            db.session.add(user)
            db.session.commit()
            return {"result":"success"}
        else:
            return re.errors