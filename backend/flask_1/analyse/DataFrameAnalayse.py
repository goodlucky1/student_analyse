from audioop import avgpp, avg

import findspark

findspark.init()
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import *
spark = SparkSession.builder.appName('hello').master('local[*]').getOrCreate()
#行号生成函数
def rownumber(counts):
    pass
def avgmethods(self,val):
    #求列平均
    return self.select(avg(val).alias(f"列{val}的平均值"))
# def avgmethods(data:DataFrame,val):
#     #求列平均
#     return data.select(avg(val).alias(f"列{val}的平均值"))
def avgrowmethods(data:DataFrame,idname,*args):
    #行平均
    return data.selectExpr(idname,'+'.join([str(elem) for elem in args])+'as `平均分`')

def scoresubject(data:DataFrame,course):
    # 统计分数段
    data.withColumn('score_range')
df = spark.read.jdbc("jdbc:mysql://10.10.209.221:3306/studb?useSSL=false","people",properties={'user':'root','password':'Password123$'})
# df.select(avg('`成绩`')).show()
# df.selectExpr('`信息技术基础`+`C#程序设计` as `平均分`').show()
avgrowmethods(df,'`姓名`',"`信息技术基础`","`C#程序设计`","`HTML5+CSS3技术基础`").orderBy('平均分').show()
scoresubject(df,'`信息技术基础`')