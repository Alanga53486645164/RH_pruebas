import pymysql
from colorama import init, Fore, Back, Style
from open import SQLFile
# import os

# os.chdir('./')

# create database cuentan;
# use cuentan;


class Conexion:
    conn=None
    archivoVersion='dbVersion.txt'
    print=True
    cursor=None
    db=None
    fetch=None
    n_cols=None
    n_tab=None

    instrucciones=["use","insert","select","update","delete"]
    
    def __init__(self,database,version,archivoSQL):
        self.ConexionSQL()
        self.db=database

        self.version=version
        self.archivoSQL=archivoSQL
        
        self.cursor = self.conn.cursor()


        self.conectarDB(self.getArchivoVersionDB())
    
    def getArchivoVersionDB(self):
        try:
            return open(self.archivoVersion,'r').read()
        except Exception:
            open(self.archivoVersion,'x')
            return ''
    
    def setNewFileVersion(self,version):
        open(self.archivoVersion,'w').write(version)
    
    def ConexionSQL(self):
        try:
            self.conn= pymysql.connect(host='localhost', user='root', password="risemivicio125")
            #    print("Conexion 1")
        except Exception:
            self.conn= pymysql.connect(host='localhost', user='root', password="")
            #    print("Conexion 2")
            
    def execute_query(self,query):
        try:
            #print(Back.MAGENTA+query+Back.RESET)
            if( self.print):
                print(query)
            else:
                print(query[:20])
            ##Ejecuta la consulta
            self.cursor.execute(query)
            #continua si la expresion es posible
            
            #detecta la instruccion principal de la consulta
            c=self.detectar_Instruccion(query)
            print(f"{Back.CYAN}___Consulta exitosa{Back.RESET}")

            #    print(f"c={c}")
            if c==2:
                self.fetch=self.cursor.fetchall()
            else:
                self.conn.commit()
                
            return 1
        except Exception:
            ##consulta mal formulada o imposible
            if( self.print==False):
                print(query)
            print(f"{Back.RED}____________>Fallo La consulta{Back.RESET}")
            print()
            return -1
        
    def detectar_Instruccion(self,query):
        #    print("  __det consult")
        query=query.lower()    
        SinEspacios=query.replace(" ","")

        c=0
        
        for inst in self.instrucciones:
            if((SinEspacios.split(inst))[0]==""):
                return c
            c+=1
    
    def executeSQLFile(self):
        self.file=SQLFile()
        self.showQuery(False)
        with open(self.archivoSQL, "r",encoding="utf-8") as archivo:
            c=0
            ba=None
            while True:
                self.instrucciones=self.file.getSQLines(archivo)
                print(c)

                for i in self.instrucciones: 
                    self.execute_query(i)
                
                if self.instrucciones==[''] or self.instrucciones==[]:
                    break
                c+=1
        self.showQuery(True)

    def crear_DB(self,extension):
        if(extension!=''):
            extension=f'_{extension}'
        self.execute_query(f"drop schema if exists {self.db+extension}")
        self.execute_query(f"create schema {self.db+extension}")
        self.execute_query(f"use {self.db+extension}")

        query='create table version( version int not null);'
        self.execute_query(query)
        query='insert into version values(%s);'%(self.version)
        self.execute_query(query)

        self.executeSQLFile()

        # self.crear_tablas()

    def getFromVersion(self):
        r=self.execute_query('select version from version')
        if r==-1:
            return None
        return self.getFetch()[0]
        
    def conectarDB(self,extension):
        # print("\n\n\n CONECTAR")
        print('conectar')
        use="use "+self.db
        if extension!='':
            use+=f'_{extension}'

        if self.execute_query(use)==-1:
            print('No existe la db')
            #fallo la conexion a la db
            #no existe
            if self.getArchivoVersionDB()!=extension:
                # la extension/version libre de la db no concuerda con la marcada en el archivo de Version
                self.setNewFileVersion(extension)

            self.crear_DB(extension)
            return 
        #existe la db
        print("EXISTE LA DB")

        #select a la tabla version en la DB
        ver=self.getFromVersion()
        if ver ==None:
            print('no es nuestra db(no existe tabla version)')
            #no esta agregada la tabla de version, es decir, no es nuestra base de datos
            if extension=="": 
                #es el primer fallo
                self.conectarDB("1")
            else: 
                #ya van varias bd a las que se intento conectar
                self.conectarDB(str(int(extension)+1))
            return
        print(f'VERSION ={ver[0]}')
        print(f'VERSION 2 ={self.version}')

        if int(ver[0])!=int(self.version):
            print('la db esta desactualizada')
            # el campo version en la DB no concuerda con el que deberia ser
            self.crear_DB(extension)
            return 
        else:
            print('DB ACTUAL SIN NECESIDAD DE CAMBIOS')

    def getFetch(self):
        return self.fetch
    
    def reiniciarContatorAuto(self,tabla):
        self.execute_query(f"ALTER TABLE {tabla} AUTO_INCREMENT=0")
    
    def close(self):
        self.conn.close()
        self.cursor.close()
    
    def showQuery(self,booleano):
        self.print=booleano