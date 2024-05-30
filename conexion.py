import pymysql
def conectar():
    return pymysql.connect(host='localhost', user='root', passwd='', db='rh3')


