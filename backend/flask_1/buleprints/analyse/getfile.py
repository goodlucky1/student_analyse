import json

from flask import Blueprint,request
import openpyxl
import pandas as pd
from flask_dbobject.dbobject import db
from sparkproject.pandastojson import *

bp = Blueprint('getfile', __name__,url_prefix='/getfile')



@bp.route('/',methods=['GET','POST'])
def getfile():
    if request.method == 'GET':
        pass
        # return "success"
    elif request.method == 'POST':
        res= request.files.getlist("file")
        for file in res:
            df = pd.read_excel(file)
            pandastodb(df,'10.10.209.221','root','Password123$','studb')
            return json.dumps(pandastojson(df),ensure_ascii=False,indent=4)

            # file_content= file.read()
            # content_str = file_content
            # print(content_str)

        # return "success"
