from flask import Blueprint,request,session
from werkzeug.datastructures import MultiDict
from wtforms import Form, StringField, IntegerField, validators,EmailField
from wtforms.validators import ValidationError
from flask_model import model
from flask_dbobject.dbobject import db


#length -min max message
#EqualTo password_repeat = StringField(validators=[Length(min=6,max=10),EqualTo("password")])
#Email
#InputRequired
#NumberRange
#Regexp 正则(r'1[34578]\d{9}')手机号验证
#URL
#UUID
#    def  validate_username(self,field):
#        print(field.data)
#        if field.data =="123":
#            raise ValidationError("error")
#


class LoginForm(Form):
    username = StringField("username", validators=[validators.Length(min=3, max=100, message="this length is 3 to 100"),
                                                   validators.DataRequired("this is required")])
    password = StringField("password", validators=[validators.Length(min=6, max=100, message="this length is 6 to 100"),
                                                   validators.DataRequired(message="this is required")])


bp = Blueprint('login', __name__, url_prefix='/login')





@bp.route("/",methods=['GET','POST'])
def index():
    if request.method == "GET":
        return {"result":"success"}
    elif request.method == "POST":
        re= LoginForm(MultiDict(request.get_json()))
        if re.validate():
            username = request.get_json().get("username")
            password = request.get_json().get("password")
            user= model.User.query.filter(model.User.username == username, model.User.password == password).first()
            if user:
               return {"result":"login success"}
            return {"result":"login failed"}
        else:
            return re.errors

