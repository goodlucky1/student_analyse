import pandas as pd
import pymysql
from sqlalchemy import engine, create_engine

from MysqlTool import MysqlTool


class PandasToDb(MysqlTool):
    def __init__(self,username,password,hostname,database):
        self.username = username
        self.password = password
        self.hostname = hostname
        self.database = database
        pass
    def pandasTodb(self,df,tablename):
        #pandas存入数据库
        for col in df.columns:
            df[col] = df[col].astype(str)
        pymysql.install_as_MySQLdb()
        DB_STRING = f'mysql+mysqldb://{self.username}:{self.password}@{self.hostname}/{self.database}?charset=utf8'
        engine = create_engine(DB_STRING)
        df.to_sql(tablename, con=engine, if_exists='replace', index=False)
    def altertablename(self,oldname,newname):
        con = pymysql.connect(host=self.hostname,user=self.username,password=self.password,database=self.database)
        conn = con.cursor()
        conn.execute(f"alter table {oldname} rename to {newname}")
        con.commit()
        conn.close()
        con.close()
    def droptable(self,tablename):
        con = pymysql.connect(host=self.hostname, user=self.username, password=self.password, database=self.database)
        conn = con.cursor()
        conn.execute(f"drop table {tablename}")
        con.commit()
        conn.close()
        con.close()
    def truncatetable(self,tablename):
        con = pymysql.connect(host=self.hostname, user=self.username, password=self.password, database=self.database)
        conn = con.cursor()
        conn.execute(f"truncate table {tablename}")
        con.commit()
        conn.close()
        con.close()
    def showtables(self):
        super().selected(f"show tables in {self.database}")
    #按列抽取
    def selectexcelcolumns(*args):
        df = pd.read_excel('D:\\Lenovo\\PycharmProjects\\BackTools\\ExcelToCsv\\1733488998.40417.xlsx')

        return df[[item for item in args]]

if __name__ == '__main__':
    PandasToDb('root','Password123$','10.10.209.221','studb').showtables()