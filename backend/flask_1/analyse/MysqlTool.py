import pymysql
class MysqlTool(object):
    def __init__(self, hostname, username, password, port=3306):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.port = port


    def selected(self,sqlstr):
        con = pymysql.connect(host=self.hostname,user=self.username,password=self.password)
        conn = con.cursor()
        conn.execute(sqlstr)
        header = [i[0] for i in conn.description]
        fetchall = conn.fetchall()
        jsonobj = []
        for i in range(len(fetchall)):
            record = {}
            for j in range(len(header)):
                record[header[j]] = fetchall[i][j]
            jsonobj.append(record)
        con.commit()
        # print(jsonobj)
        conn.close()
        con.close()
        return jsonobj
dictconnect = {'host': '10.10.209.221',
                   'user': 'root',
                   'password': 'Password123$',
                   'port': 3306,
                   }
# if __name__ == '__main__':
#     MysqlTool('localhost', 'root', 'Password123$', '<PASSWORD>', 3306).selected(dictconnect)