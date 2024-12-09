from flask import Flask
import flask_config.config
from flask_dbobject.dbobject import db
from flask_migrate import Migrate
from buleprints.base.login import bp as login_bp
from buleprints.base.registry import bp as registry_bp

#所需依赖包 flask_migrate flask_sqlalchemy flask_cors pymysql flask-wtf
app = Flask(__name__)
#
app.debug=True


#app配置信息
app.config.from_object(flask_config.config)
#初始化数据库
db.init_app(app)
#配置ORM
migrate = Migrate(app, db)

#注册蓝图
app.register_blueprint(login_bp)
app.register_blueprint(registry_bp)
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
