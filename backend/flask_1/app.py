import json

from flask import Flask, request
import flask_config.config
from flask_dbobject.dbobject import db
from flask_migrate import Migrate
from buleprints.base.login import bp as login_bp
from buleprints.base.registry import bp as registry_bp
from buleprints.analyse.getfile import bp as get_file_bp
from flask_cors import CORS

#所需依赖包 flask_migrate flask_sqlalchemy flask_cors pymysql flask-wtf
app = Flask(__name__)
#
app.debug=True

#允许跨域
CORS(app, resources={r"/*": {"origins": "*", "supports_credentials": True}})

#app配置信息
app.config.from_object(flask_config.config)
#初始化数据库
db.init_app(app)
#配置ORM
migrate = Migrate(app, db)
#设置cookie失效时间
app.permanent_session_lifetime=1000*60*60*24*7
#注册蓝图
app.register_blueprint(login_bp)
app.register_blueprint(registry_bp)
app.register_blueprint(get_file_bp)

import os
@app.route('/',methods=['GET','POST'])
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
