import pymysql
def conectar():
    try:
        return pymysql.connect(host='localhost', user='root', passwd='risemivicio125', db=open('db.txt','r').read())
    except:
        print('____________ERROR AL CONECTAR A:__',open('db.txt','r').read())

