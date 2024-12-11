from flask import Blueprint,request
import openpyxl
import pandas as pd
from flask_dbobject.dbobject import db
bp = Blueprint('getfile', __name__,url_prefix='/getfile')



def create_table_from_df2(df,table_name):
    class DynamicTable(db.Model):
        __tablename__ = table_name
        id = db.Column(db.Integer, primary_key=True)
        columns=[]
        for col in df.columns:
           columns.append(db.Column(col, db.String(255)))
        locals().update({col:column for col,column in zip(df.columns, columns)})

    db.create_all()
    return DynamicTable

@bp.route('/',methods=['GET','POST'])
def getfile():
    if request.method == 'GET':
        return "success"
    elif request.method == 'POST':
        res= request.files.getlist("file")
        for file in res:
            df = pd.read_excel(file)
            print(df)

            # file_content= file.read()
            # content_str = file_content
            # print(content_str)

        return "success"
