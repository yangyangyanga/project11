import pymysql

class YangMySQL():
    def __init__(self, host, user, passwd, dbName):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.dbName = dbName
    def connect(self):
        self.db = pymysql.connect(self.host, self.user, self.passwd, self.dbName)
        self.cursor = self.db.cursor()
    def close(self):
        self.cursor.close()
        self.db.close()

    def get_one(self, sql):
        res = None
        try:
            self.connect()
            self.cursor.execute(sql)
            res = self.cursor.fetchone()
            self.close()
        except:
            print("查询失败")
        return res

    def get_all(self, sql):
        res = ()
        try:
            self.connect()
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            self.close()
        except:
            print("查询失败")
        return res

    def get_all_obj(self, sql, tableName, *args):
        resList = []
        fieldsList = []
        # 获得列名
        if(len(args) > 0):
            for item in args:
                fieldsList.append(item)
        else:
            fieldsSql = "select COLUMN_NAME from information_schema.COLUMNS where table_name = '%s'and table_schema='%s'"%(tableName, self.dbName)
            fields = self.get_all(fieldsSql)
            for item in fields:
                fieldsList.append(item[0])

        # 获得表数据
        res = self.get_all(sql)
        for item in res:
            obj = {}
            count = 0
            for x in item:
                obj[fieldsList[count]] = x
                count += 1
            resList.append(obj)
        return resList

    def insert(self, sql):
        return self.__edit(sql)
    def update(self, sql):
        return self.__edit(sql)
    def delete(self, sql):
        return self.__edit(sql)
    def __edit(self, sql):
        count = 0
        try:
            print("------1")
            self.connect()
            print("------2")
            count = self.cursor.execute(sql)
            print("------3", count)
            self.db.commit()
            print("------4")
            self.close()
        except:
            print("事物提交失败")
            self.db.rollback()
        return count



