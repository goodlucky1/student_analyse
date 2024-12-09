from flask_dbobject.dbobject import db

class UserRole(db.Model):
    __tablename__ = 'userrole'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userRole = db.Column(db.String(128), nullable=False,unique=True)
    roleLevel = db.Column(db.Integer, nullable=False)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(512), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    userRole = db.Column(db.String(128),db.ForeignKey('userrole.userRole'), nullable=False)





