import pymysql
def conectar():
    return pymysql.connect(host='localhost', user='root', passwd='risemivicio125', db='rh3_2')


