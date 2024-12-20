import json


import openpyxl
import pandas as pd

from analyse import PandasToDb as pandasToDb
from analyse import Selectedtable as selectedtable
import time



def createdf(df,hostname,username,password,database):
    try:
        current = str(int(time.time()))
        stu_db = pandasToDb.PandasToDb(username, password, hostname, database)
        stu_db.pandasTodb(df, current)
        return current
    except Exception as e:
        print("error", e)
        return "fail"

def insert(data,hostname,username,password,database,table):
    try:
        stu_db = pandasToDb.PandasToDb(username, password, hostname, database)
        res=stu_db.insertTodb(data,database,table)
        return res
    except Exception as e:
        print("error",e)
        return "fail"

def select(hostname,username,password,database,table,start,size):
    try:
        select_db = selectedtable.SelectedTable(hostname, username, password)
        change = select_db.selectoffset(database, table, start, size)
        lines =select_db.selectlines(database, table)
        data={
            "change":change,
            "lines":lines
        }
        print(data)
        return data
    except Exception as e:
        print("error",e)
        data = {
            "change":"fail"
        }
        return data

def selectByWhere(hostname,username,password,database,table,where):
    try:
        select_db = selectedtable.SelectedTable(hostname, username, password)
        data= select_db.selected_header("select * from " + database+"."+table)

        data=[f"{da} LIKE '%{where}%'" for da in data]
        data=" or ".join(data)
        sql =f"select * from {database}.{table} where "+data

        res=select_db.selected(sql)

        return res
    except Exception as e:
        print("error",e)
        data = {
            "change": "fail"
        }
        return data

def update(data,data2,hostname,username,password,database,table,union):
    try:
        res=delete(data2,hostname,username,password,database,table,union)
        if res>0:
            res=insert(data,hostname,username,password,database,table)
            return res
        else:
            return "fail"
    except Exception as e:
        print("error",e)
        return "fail"


def delete(data,hostname,username,password,database,table,union):
    try:
        select_db = selectedtable.SelectedTable(hostname, username, password)

        data=[f"{union}='{da}'" for da in data]
        sql=' or '.join(data)
        res=select_db.updated_delete(f"delete from {database}.{table} where "+sql)
        return res
    except Exception as e:
        print("error",e)
        return "fail"
