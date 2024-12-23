import json
from audioop import avgpp, avg

import findspark
from pyspark import StorageLevel

findspark.init()
from pyspark.sql import SparkSession, DataFrame, Window
from pyspark.sql.functions import *
spark = SparkSession.builder.appName('hello').master('local[*]').getOrCreate()
#行号生成函数
def rownumber(counts):
    pass
# def avgmethods(self,val):
#     #求列平均
#     return self.select(avg(val).alias(f"列{val}的平均值"))
def avgmethods(data:DataFrame,val):
    #求列平均
    rows = data.persist(StorageLevel.MEMORY_AND_DISK).select(avg(val).alias(f"列{val}的平均值")).collect()
    row_dicts = [convert_values_to_str(row.asDict()) for row in rows]
    return row_dicts
def avgrowmethods(data:DataFrame,idname,*args):
    rows = data.persist(StorageLevel.MEMORY_AND_DISK).selectExpr(idname,'+'.join([str(elem) for elem in args])+'as `平均分`').collect()
    row_dicts = [convert_values_to_str(row.asDict()) for row in rows]
    return row_dicts
def convert_values_to_str(row_dict):
    #字典值全都转化成str
    return {k: str(v) for k, v in row_dict.items()}
#行转列
def rowtocolumn(data:DataFrame,config,name):
    # data.where(f"{config}='{name}'").withColumn('`课程名`',data.where(f"{config}='{name}'"))
    pass
#某一课程的排名
def rankcourse(data:DataFrame,course):
    column = data.persist(StorageLevel.MEMORY_AND_DISK).select("`姓名`", course).withColumn("排名", dense_rank().over(Window.orderBy(col(course).desc())))
    rows = column.collect()
    return [convert_values_to_str(row.asDict()) for row in rows]
def scoresubject(data:DataFrame,course):
    # 统计分数段
    rows =  (data.persist(StorageLevel.MEMORY_AND_DISK).selectExpr(course)
            .withColumn('score_range',when(col(course)<60,'不及格')
                           .otherwise(when((col(course)>=60) & (col(course)<=70),'60到70')
                        .otherwise(when((col(course)>70) & (col(course)<=80),'70到80')
                        .otherwise(when((col(course)>80) & (col(course)<=90),'80到90')
                    .otherwise(when(col(course)>90,'90以上'))))))
            .groupby('score_range')
            .agg(count('score_range').alias('student_count'))
            .selectExpr(f'score_range as {course}', 'student_count')).collect()
    row_dicts = [convert_values_to_str(row.asDict()) for row in rows]
    return row_dicts
df = spark.read.jdbc("jdbc:mysql://10.10.209.221:3306/studb?useSSL=false","stu_log",properties={'user':'root','password':'Password123$'})
print(df.columns)
# df.persist(StorageLevel.MEMORY_AND_DISK)
# df.show()
# print(json.dumps(rankcourse(df, '`HTML5+CSS3技术基础`'), indent=4,ensure_ascii=False))
# rowtocolumn(df,'`姓名`','高诗曼')
# df.where("`姓名`='高诗曼'").show()
# df.select(avg('`成绩`')).show()
# df.selectExpr('`信息技术基础`+`C#程序设计` as `平均分`').show()
# avgrowmethods(df,'`姓名`',"`信息技术基础`","`C#程序设计`","`HTML5+CSS3技术基础`").orderBy('平均分').show()
# print(scoresubject(df, '`C#程序设计`'))
# print(json.dumps(scoresubject(df, '`C#程序设计`'), indent=4, ensure_ascii=False))