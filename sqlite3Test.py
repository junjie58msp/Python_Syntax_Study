# coding:utf-8
# jayjayli
# python 如何连接sqlite数据库
# 操作数据库常用方法
# https://www.runoob.com/sqlite/sqlite-python.html
import os,sys,time
import sqlite3

def createTable(dbnamein, tablenamein):
    '''
    打开 dbnamein 数据库
    确认表 tablenamein 是否存在
    如果不存在则创建
    '''
    pass


def findalltablesindb(dbnamein):
    '''
    打开表 dbnamein
    然后找出此db里面的所有表名
    https://docs.qq.com/doc/DWlJiUUpBZk5Bd21j
    '''
    print 'dbname is: '+dbnamein
    try:
        connection = sqlite3.connect(dbnamein)
        cursor = connection.cursor()
        cmd_get_tablename = "select name from sqlite_master where type='table' order by name"
        cmdresult = cursor.execute(cmd_get_tablename)
        # for i in result:
        #     print i 
        result = cmdresult.fetchall()
        print result,len(result)
        connection.close()
    except Exception,e:
        print 'can not open db: '+dbnamein
        print e

def findallfieldintables(dbnamein):
    '''
    打开表 dbnamein
    找出此db中所有表，以及里面的所有字段的名称 //找表参照： findalltablesindb
    返回：表字段，表名
    这里表字段的构成是： [[表一的所有字段，表名称]]
    '''
    print 'dbname is: '+dbnamein
    try:
        connection = sqlite3.connect(dbnamein)
        cursor = connection.cursor()
        cmd_get_tablename_in_db = "select name from sqlite_master where type='table' order by name;"
        cmdresult = cursor.execute(cmd_get_tablename_in_db)
        # for i in result:
        #     print i 
        alltable = cmdresult.fetchall()
        alltable.sort()
        allfiledresult =[]
        for table in alltable:
            eachtable = table[0].encode("utf-8")    # (u'FM_Account',)  每个table的结果是一个truple
            cursor.execute("PRAGMA table_info("+eachtable+")")
            cmd_result = cursor.fetchall()
            cmd_result.append(eachtable) # 再把每张表的名字插入到最后位置
            allfiledresult.append(cmd_result)
        connection.close()
    except Exception,e:
        print 'can not open db: '+dbnamein
        print e    
    print allfiledresult
    return allfiledresult, alltable


if __name__ == "__main__":
    #findalltablesindb('./testResource/FMailDB.db')
    findallfieldintables('./testResource/FMailDB.db')
