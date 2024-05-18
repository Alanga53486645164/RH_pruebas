import pymysql
from colorama import init, Fore, Back, Style
# import inserts

db="rh3"

# create database cuentan;
# use cuentan;


class Conexion:
    conn=None
    cursor=None
    db=None
    fetch=None
    n_cols=None
    n_tab=None

    instrucciones=["use","insert","select","update","delete"]
    
    def __init__(self,database,num_columns,num_tablas):
        self.ConexionSQL()
        self.n_tab=num_tablas
        self.db=database
        self.n_cols=num_columns
        self.cursor = self.conn.cursor()

        self.conectarDB("")

    def ConexionSQL(self):
        try:
            self.conn= pymysql.connect(host='localhost', user='root', password="risemivicio125")
            #    print("Conexion 1")
        except Exception:
            self.conn= pymysql.connect(host='localhost', user='root', password="")
            #    print("Conexion 2")
            
    def execute_query(self,query):
        try:
            print(Back.MAGENTA+query+Back.RESET)
            ##Ejecuta la consulta
            self.cursor.execute(query)
            #continua si la expresion es posible
            
            #detecta la instruccion principal de la consulta
            c=self.detectar_Instruccion(query)
            print(f"{Back.CYAN}___Consulta exitosa{Back.RESET}")

            #    print(f"c={c}")
            if c==1 or c==3 or c==4:
                #insert,update
                self.conn.commit()
            elif c==2:
                #select
                self.fetch=self.cursor.fetchall()
            #     return self.fetch
                
            return 1
        except Exception:
            ##consulta mal formulada o imposible
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

    # def inserts(self):
    #     tablas=(
    #         "productos(nombre,categoria,   n_ventas,precio,existencias,descripcion,img_presentacion)",
    #     )

    #     #categorias: ('CONSOLAS'),('AUDIFONOS'),('MANDOS'),('TELEVISIONES'),('CELULARES'),('VIDEOJUEGOS')

    #     #plataformas: ("XBOX ONE"), ("XBOX ONE SERIES X/S"), ("XBOX 360"), ("PLAY STATION 2"), ("PLAY STATION 3"),
    #     #             ("PLAY STATION 4"), ("PLAY STATION 5"), ("NINTENDO SWITCH"), ("PC"), ("CELULAR")
    #     queries=inserts.getQueries()
    #     print(queries)
    #     for c in range(0,len(queries)):
    #         print("tabla= ",tablas[c])
    #         for insert in queries[c]:
    #             if( len(insert) ==5):
    #                 in3=3
    #             else:
    #                 in3=2
                
    #             self.execute_query(f'INSERT INTO {tablas[c]} values( {insert[0]}  , {insert[1]} , {insert[in3]} )')

    #             if(insert[1]==6):
    #                 query_plata='INSERT INTO videojuego_has_plataforma VALUES'
    #                 c2=0
    #                 self.execute_query(f'select codigo from productos where nombre={insert[0]}')
    #                 id=self.getFetch()[0][0]

    #                 for plataforma in insert[2]:

    #                     query_plata+=f"({id},{plataforma})"
    #                     if( c2 < len(insert[2])-1 ):
    #                         query_plata+=","
    #                     c2+=1
    #                 self.execute_query(query_plata)
                    
    #             if(len(insert[4])!=0):
    #                 c2=0
    #                 query="INSERT INTO imagenes_productos(direccion,codigo_producto) VALUES"
    #                 for liga in insert[4]:
    #                     query+=f"({liga},{id})"
    #                     if( c2 < len(insert[4])-1 ):
    #                         query+=","
    #                     c2+=1
    #                 self.execute_query(query)
                
    def crear_tablas(self):
        instrucciones=("CREATE TABLE","INSERT INTO")

    def crear_DB(self,extension):
        self.execute_query(f"create schema {self.db+extension}")
        self.execute_query(f"use {self.db+extension}")
        self.crear_tablas()

    def conectarDB(self,extension):
        # print("\n\n\n CONECTAR")
        use="use "+self.db+extension
        if self.execute_query(use)==-1:
            #fallo la conexion a la db
            #no existe
            self.crear_DB(extension)
        # else:
        #     #existe la db
        #     #    print("EXISTE LA DB")
        #     query=f"SELECT count(*) FROM information_schema.columns WHERE table_schema = '{self.db+extension}' AND table_name = 'cuentas'"
        #     self.execute_query(query)
        #     result1=self.getFetch()[0][0]

        #     query=f"SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = '{self.db+extension}';"
        #     self.execute_query(query)

        #     result2=self.getFetch()[0][0]

        #     # print(f"\n\nRestult={result1} ? {self.n_cols}      ;     result2={result2} ? {self.n_tab}")

        #     if(result1==self.n_cols and result2==self.n_tab):
        #         #la db coincide en numero de tablas, y columnas de la tabla cuentas
        #         query="select count(*) from cuentas where nombre and telefono and edad and id_cuenta and email and psw and foto_perfil"
        #         resu=self.execute_query(query)
        #         print("______>",resu)
        #         if(resu!=-1):
        #             #    print("\nES LA DB CORRECTA\n")
        #             #la database es correcta, en campos y longuitud
        #             return None
        #         # print("\n\nPUNTO 1")
        #         self.execute_query(f"drop schema {self.db}")
        #         self.crear_DB(extension)
        #         return None
        #     # print("\n\nPUNTO 2")
        #     if extension=="":
        #         # print("\n\nPUNTO ")

        #         #    print("\nPRIMER FALLO\n")
        #         #es el primer fallo
        #         self.conectarDB("1")
        #     else:
        #         # print("\n\nPUNTO 3")
        #         #    print("\nFALLO N\n")
        #         #ya van varias bd a las que se intento conectar
        #         self.conectarDB(str(int(extension)+1))

    def getFetch(self):
        return self.fetch
    
    def reiniciarContatorAuto(self,tabla):
        self.execute_query(f"ALTER TABLE {tabla} AUTO_INCREMENT=0")
    
    def close(self):
        self.conn.close()
        self.cursor.close()


# cx=Conexion("cuentan",7,8)

# cx.inserts()
# cx.execute_query("drop schema cuentan")