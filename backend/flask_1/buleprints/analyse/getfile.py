import json
<<<<<<< HEAD
=======
import time
>>>>>>> 38687b2f650abbcbec668ccd5823911306e91b93

from flask import Blueprint,request
import openpyxl
import pandas as pd
from sqlalchemy.orm.sync import update

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
<<<<<<< HEAD
        for file in res:
            df = pd.read_excel(file)
            pandastodb(df,'10.10.209.221','root','Password123$','studb')
            return json.dumps(pandastojson(df),ensure_ascii=False,indent=4)
=======
        df = pd.read_excel(res[0])

        from buleprints.analyse.tableData import createdf
        res= createdf(df, "10.10.210.154", "root", "Password123$", "db")
        if res=="success":
            data={
                "status":"success create data",
                "tableName":res
            }
            return data
        data = {
            "status": "fail create data"
        }
        return data


@bp.route('/insert',methods=['POST'])
def insert():
    data=json.loads(json.dumps(request.get_json()))
    data=dict(data)
    tableName=data['tableName']
    data.pop("tableName")
    from buleprints.analyse.tableData import insert
    res=insert(data["data"],"10.10.210.154", "root", "Password123$", "db",tableName)
    if res!="fail":
        data2={
            "status":"success insert data",
            "data":data
        }
        return data2
    data2 = {
        "status": "fail insert data",
        "data": data
    }
    return data2

@bp.route('/select',methods=['POST'])
def select():
    start=request.get_json().get("start")
    size=request.get_json().get("size")
    tableName=request.get_json().get("tableName")

    from buleprints.analyse.tableData import select
    res=select("10.10.210.154", "root", "Password123$", "db",tableName,start,size)
    if res.get("change")!="fail":
        data2={
            "status":"success select data",
            "data":res.get("change"),
            "lines":res.get("lines")
        }
        return data2
    data2 = {
        "status": "fail select data",
    }
    return data2

@bp.route('/selectByWhere',methods=['POST'])
def selectByWhere():
    where=request.get_json().get("where")
    tableName=request.get_json().get("tableName")
    from buleprints.analyse.tableData import selectByWhere
    res=selectByWhere("10.10.210.154", "root", "Password123$", "db",tableName,where)
    if type(res)==type("1"):
        res=-1
    if res!=-1:
        data = {
            "status": "success select data",
            "data": res
        }

        return res
    data = {
        "status": "fail select data"
    }
    return data

@bp.route('/update',methods=['POST'])
def update():
    data = json.loads(json.dumps(request.get_json()))
    data = dict(data)
    tableName = data['tableName']
    data.pop("tableName")
    union = data['union']
    data.pop("union")
    data2=[data["data"][union]]

    from buleprints.analyse.tableData import update
    res=update(data["data"],data2,"10.10.210.154", "root", "Password123$", "db",tableName,union)
    if type(res)==type("1"):
        res=0
    if res>0:
        data2={
            "status":"success update data",
            "data":data
        }
        return data2
    data2 = {
        "status": "fail update data",
        "data": data
    }
    return data2

@bp.route('/delete',methods=['POST'])
def delete():

    data=json.loads(json.dumps(request.get_json()))
    tableName = data['tableName']
    data.pop("tableName")
    union = data['union']
    data.pop("union")

    from buleprints.analyse.tableData import delete

    res= delete(data["data"],"10.10.210.154", "root", "Password123$", "db",tableName,union)
    if type(res)==type("1"):
        res=0
    if  res>0:
        data2={
            "status":"success delete data",
            "data":data
        }
        return data2
    data2 = {
        "status": "fail delete data",
        "data": data
    }
    return data2

>>>>>>> 38687b2f650abbcbec668ccd5823911306e91b93


<<<<<<< HEAD
        # return "success"
=======
>>>>>>> 38687b2f650abbcbec668ccd5823911306e91b93
