HOSTNAME = "10.10.210.154"
PORT = "3306"
USERNAME = "root"
PASSWORD = "Password123$"
DataBase = "db"
#mysql数据连接配置
SQLALCHEMY_DATABASE_URI=f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DataBase}?charset=utf8"


SECRET_KEY="username"