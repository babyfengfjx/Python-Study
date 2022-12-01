#  将dict.txt内容存入mysql数据库
import re
import pymysql
import time
from pymysql.converters import escape_string  # 这句是做字符串转义的，下面使用escape_string来处理
# 对比另外dict2mysqlV2.py中的版本，貌似没啥效率的提升
starttime = time.time()
class Tomysql():
    """
    直接通过类来管理数据库链接，避免重复的数据库连接和断开
    """
    def __init__(self):
        self.db = pymysql.connect(host='localhost',
                             port=3306,
                             user='babyfengfjx',
                             password='123456',
                             charset='utf8',
                             database='stu')
        self.cur = self.db.cursor()
    def executes(self,info):
        sql = "insert into dict (word,explanation) values (%s,%s)"
        # sql = 'show tables;'
        try:
            self.cur.execute(sql,info)
            self.db.commit()
        except Exception as e:
            print(e)
            print(info)
            self.db.rollback()
        # res = self.cur.fetchall()
        # print(res)

    def close(self):
        """
        关闭连接
        """
        self.cur.close()
        self.db.close()

file = open('dict.txt')
mysqls = Tomysql()
for i in file:

    res = re.findall(r"(\w+\s\w+|['\w-]+)\s+(.*)",i)  # 有的单词中间有一个空格，这个时候需要把\w+\s\w+放在前面，不然会匹配不到,有点单词中间有- ，[\w-]+ 正好可以匹配到
    if res:
        res = res[0]
    # print(res)
    # word = res[0]
    # explannation = escape_string(res[-1])  # 这句是做字符串转义的，有时候存在单个引号的情况下，直接存入字符串到数据库就会报错，使用这个就可以解决问题
    # print(word,explannation)
    mysqls.executes(res)
        # print(res)
file.close()
mysqls.close()
end = time.time()
print(end-starttime)