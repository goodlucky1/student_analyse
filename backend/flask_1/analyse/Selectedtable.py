import pymysql
import hdfs
from MysqlTool import MysqlTool
def f(*args):
    s = ','.join([str(elem) for elem in args])
    print(s)
f('id','name')

class SelectedTable(MysqlTool):
    def __init__(self,hostname,username,password):
        self.hostname = hostname
        self.username = username
        self.password = password
        super().__init__(self.hostname,self.username,self.password)
        pass
    def selectall(self,database,table):
        super().selected(f"select * from {database}.{table}")
    def selectoffset(self,database,table,n,m):
        super().selected(f"select * from {database}.{table} limit {m*n-m},{m}")
    def selectmany(self,database,table,*args):
        super().selected(f"select {','.join([str(elem) for elem in args])} from {database}.{table}")
    def selectmany(self,database,table,n,m,*args):
        super().selected(f"select {','.join([str(elem) for elem in args])} from {database}.{table} limit {m*n-m},{m}")
    def selectavg(self,database,table,*args):
        super().selected(f"select `姓名`,{'+'.join([str(elem) for elem in args])}/{len(args)} as total_avg from {database}.{table}")
    def selectwhere(self,database,table,config,value):
        super().selected(f"select * from {database}.{table} where {config} = '{value}'")
if __name__ == '__main__':
    SelectedTable("10.10.209.221","root","Password123$").selectall('studb','people')
    SelectedTable("10.10.209.221","root","Password123$").selectoffset('shtd_store','order_info',2,10)
    SelectedTable("10.10.209.221","root","Password123$").selectmany('shtd_store','order_info',1,10,'id','consignee')
    SelectedTable("10.10.209.221","root","Password123$").selectavg('studb','people','`[010451]信息技术基础`','`[01060020]C#程序设计`','`[01060021]HTML5+CSS3技术基础`')
    SelectedTable("10.10.209.221","root","Password123$").selectwhere('studb','people','`姓名`','秦敬惠')

