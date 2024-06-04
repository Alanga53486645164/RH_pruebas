from conexionEquipo7 import Conexion,init, Fore, Back, Style 
from editor_texto import Editor
# from colorama import init, Fore, Back, Style

reiniciar_campos=False

class Admin(): 
    database=open('db.txt','r').read()
    version="2"
    archivoSQL='rh3_uni_nv.sql'

    def __init__(self):
        self.cx=Conexion(self.database,self.version,self.archivoSQL)
        self.editor=Editor()

    def execute(self,query):
        resu=self.cx.execute_query(query)
        return resu

    def Fetch(self):
        return self.cx.getFetch()

    def close(self):
        self.cx.close()

    def tablaPlural(self,tabla):
        # tabla + "registradas"
        print("__tabla=",tabla)
        palabras=tabla.split(" ")
        tabla2=""

        for palabra in palabras:
            tabla2+=palabra
            tabla2+=self.editor.addPlural(palabra)

            if(len(palabras)!=1):
                tabla2+=" "

        return tabla2, self.editor.isMale(tabla)

    def getArrayDatos(self):
        return self.editor.getTables(),self.editor.getIds(),self.editor.getTableTitles()

    def getTables(self):
        return self.editor.getTables()

    def tableToId(self,table):
        return self.editor.tablaToId(table)

    def tableToTitle(self,table):
        return self.editor.tablaToTitle(table)

    def titleToTable(self,title):
        return self.editor.titleToTabla(title)

    def existeTabla(self,tabla):
        return self.editor.existenciaTabla(tabla)

    def getSQLCols(self,table_name,primary_key):
        # query=f"SELECT column_name,column_key FROM information_schema.columns  WHERE table_schema = '{self.cx.db}' AND table_name = '{table_name}'"
        query=f"SELECT column_name,data_type FROM information_schema.columns  WHERE table_schema = '{self.cx.db}' AND table_name = '{table_name}'"
        if(primary_key!=True):
            query+=" and column_key !='PRI' "
        query+="order by ordinal_position"
        self.execute(query)
        return self.Fetch()

    def getSQLForeignKeysFor(self,table):
        # query=f"select COLUMN_NAME,REFERENCED_TABLE_NAME,REFERENCED_COLUMN_NAME from information_schema.KEY_COLUMN_USAGE where table_schema='rh3'and table_name='{table}' and constraint_name!='PRIMARY'"
        query=f"select COLUMN_NAME,REFERENCED_TABLE_NAME,REFERENCED_COLUMN_NAME,(select count(*) from information_schema.columns where table_schema='rh3' and table_name=referenced_table_name) as num_cols from information_schema.KEY_COLUMN_USAGE where table_schema='rh3'and table_name='{table}' and constraint_name!='PRIMARY'"
        self.execute(query)
        return self.Fetch()
        #    ('curso_has_aparicion',)
        #select COLUMN_NAME,REFERENCED_TABLE_NAME,REFERENCED_COLUMN_NAME from information_schema.KEY_COLUMN_USAGE where table_schema='rh3'and table_name='curso_has_aparicion' and constraint_name!='PRIMARY'

        #(
        #   ('id_curso', 'cursos', 'id_curso'),
        #   ('id_metodo_aplicacion', 'modo_aplicacion_curso', 'id_modo'),
        #   ('id_encargado', 'trabajadores', 'id_empleado')
        #)
    def makeJoinFor(self,table_name):
        cols=self.colsToString(table_name,False)[0]
        fk= self.getSQLForeignKeysFor(table_name)

        query=''
        c=0
        for join in fk:
            query+=f"JOIN {join[1]} ON {table_name}.{join[0]}={join[1]}.{join[2]} "
            c+=1
            
        print(f'{Fore.GREEN}cols={cols}')
        print(f'{Fore.RED}tk={fk}')
        print(f'{Back.RED}query={query}{Fore.BLACK}')
        return query
    
    def tableToSQLId(self,table_name):
        SqlIds=()
    
    def getSQLTables(self):
        query=f"select table_name from information_schema.tables where table_schema='{self.cx.db}'"
        self.execute(query)
        return self.Fetch()

    def getColsFrom(self,table_name,primary_key):
        columnas=self.getSQLCols(table_name,primary_key)
        print("\n\n")
        print(table_name,"=",columnas)
        return columnas
        # tablas=self.getSQLTables()

        # for tabla in tablas:
        #     tabla=tabla[0]
        #     columnas=self.getSQLCols(tabla)
        #     print("\n\n")
        #     print(tabla,"=",columnas)
    def colsToString(self,table,primary_key):
        return self.editor.columnsToString(self.getColsFrom(table,primary_key))

    def getColsNameFor(self,tabla):
        for tablas in self.editor.getColsName():
            if tablas.isTable(tabla):
                return tablas.getCols()
        return None

    def getComillas(self,datatype):
        # comillas="varchar","date"
        comillas="int","tinyint","double","float"
        for tipo in comillas:
            if tipo == datatype:
                return ""
        return "'"
    def searchBooleanSQL(self,array):
        c=0
        booleanos=()
        for tipo in array :
            if tipo =="tinyint":
                booleanos+=c,
            c+=1
        if len(booleanos)==0:
            return None
        return booleanos

    # def getNAcciones(self,table_name):
    #     if(table_name=='')
# admin=Admin()

# admin.makeJoinFor('curso_has_aparicion')