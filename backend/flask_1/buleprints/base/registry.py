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
    userRole=StringField("userRole", validators=[validators.DataRequired("this is not required")])

    def validate_username(self,filed):
        user= model.User.query.filter_by(username=filed.data).first()
        print(user)
        if user is not None:
            raise ValidationError("该用户已被注册")
    def validate_userRole(self,filed):
        data=["管理员","普通用户","未知用户"]
        ishas=False
        for ds in data:
            if ds==filed.data:
                ishas=True
        if not ishas:
            str="必须是 "
            for ds in data:
                if str=="必须是 ":
                    str+=ds
                else:
                    str+=","+ds
            str+=" 中的一个"

            raise ValidationError(str)

@bp.route('/', methods=('GET', 'POST'))
def index():
    if request.method == "GET":
        return {"result":"success"}
    elif request.method == "POST":
        re = RegistryForm(request.form)
        if re.validate():
            user = model.User(username=request.form.get("username"), password=request.form.get("password"),
                              email=request.form.get("email"), userRole=request.form.get("userRole"))
            db.session.add(user)
            db.session.commit()
            return {"result":"success"}
        else:
            return re.errors