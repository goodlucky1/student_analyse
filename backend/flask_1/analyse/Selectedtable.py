import pymysql
<<<<<<< HEAD
import hdfs
from MysqlTool import MysqlTool
def f(*args):
    s = ','.join([str(elem) for elem in args])
    print(s)
f('id','name')
=======

from analyse.MysqlTool import MysqlTool
>>>>>>> 38687b2f650abbcbec668ccd5823911306e91b93

class SelectedTable(MysqlTool):
    def __init__(self,hostname,username,password):
        self.hostname = hostname
        self.username = username
        self.password = password
        super().__init__(self.hostname,self.username,self.password)

    def selectall(self,database,table):
        return super().selected(f"select * from {database}.{table}")
    def selectoffset(self,database,table,n,m):
        return super().selected(f"select * from {database}.{table} limit {n},{m}")
    def selectmany(self,database,table,*args):
        return super().selected(f"select {','.join([str(elem) for elem in args])} from {database}.{table}")
    def selectmany(self,database,table,n,m,*args):
        return super().selected(f"select {','.join([str(elem) for elem in args])} from {database}.{table} limit {m*n-m},{m}")
    def selectavg(self,database,table,*args):
        return super().selected(f"select `姓名`,{'+'.join([str(elem) for elem in args])}/{len(args)} as total_avg from {database}.{table}")
    def selectwhere(self,database,table,config,value):
        return super().selected(f"select * from {database}.{table} where {config} = '{value}'")
    def selectlines(self,database,table):
        return super().selected(f"select count(*) from {database}.{table}")
