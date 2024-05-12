class Tabla:
    def __init__(self,nombre_tabla,titulo_campos):
        self.columnas=titulo_campos
        self.nombres=nombre_tabla
        self.separar_nombres()

    def isTable(self,tabla):
        try:
            self.nombres.index(tabla)
            return True
        except Exception:
            return False
    
    def separar_nombres(self):
        self.nombres=self.nombres.split(",")

    def getCols(self):
        print("tablas_cols=",self.columnas)
        return self.columnas
    
class Editor:
    def __init__(self):
        self.tablas=None
        self.titulos=None
        self.ids=None
    
    def getMasculinos(self):
        return ["Idioma","Grado de Avance","Estado Civil","Curso"]
    
    def getIds(self):
        return ["idArea","idCarrera","idEscolaridad","idEstadoCivil","idGradoAvance","idHabilidad","idIdioma","id_curso"]
    
    def getTables(self):
        return ["area","carrera","escolaridad","estado_civil","grado_avance","habilidad","idioma","cursos"]
    
    def getColsName(self):
        # Nota:No se incluye al campo ID
        tabl=Tabla("cursos",('nombre','descripcion','duracion','objetivos de aprendizaje','obligatorio'))
        tabl2=Tabla("area,carrera,escolaridad,estado_civil,grado_avance,habilidad,idioma",('Descripcion',))
        return (
            tabl,tabl2
        )

    def getTableTitles(self):
        return ["Area","Carrera","Escolaridad","Estado Civil","Grado de Avance","Habilidad","Idioma","Curso"]
    
    def isVowel(self,letra):
        vocales=["a","e","i","o","u"]
        try:
            vocales.index( letra )
            return True
        except Exception:
            return False
    
    def endsVowel(self,word):
        return self.isVowel(word[len(word)-1])
    
    def addPlural(self,palabra):
        if(palabra=="Avance" or palabra =="de"):
            return ""

        if(self.endsVowel(palabra)):
            return "s"
        
        return "es"
    
    def isMale (self,word):
        # titulos=["Area","Carrera","Escolaridad","Estado Civil","Grado de Avance","Habilidad","Idioma"]
        masculinos=self.getMasculinos()

        try:
            masculinos.index(word)
            return True
        except Exception:
            return False
        
    def tablaToTitle(self,tabla):
        if(self.tablas==None):
            self.tablas=self.getTables()
            
        try:
            c=self.tablas.index(tabla)

            if(self.titulos==None):
                self.titulos=self.getTableTitles()
            return self.titulos[c]
        except Exception:
            return None
        
    def titleToTabla(self,titulo):
        if(self.titulos==None):
            self.titulos=self.getTableTitles()

        try:
            c=self.titulos.index(titulo)
    
            if(self.tablas==None):
                self.tablas=self.getTables()
            return self.tablas[c]
        except Exception:
            return None
    
    def tablaToId(self,nombre_tabla):
        if(self.tablas==None):
            self.tablas=self.getTables()

        try:
            c=self.tablas.index(nombre_tabla)

            if(self.ids==None):
                self.ids=self.getIds()
            return self.ids[c]
        except Exception:
            return None
        
    def existenciaTabla(self,tabla):
        if(self.tablas==None):
            self.tablas=self.getTables()

        try:
            c=self.tablas.index(tabla)
        except Exception:
            print("ERROR, NO ESTÁ")
            return None
        return True    
    
    def columnsToString(self,array):
        #vacante = (('conseVR', ''), ('fuenteCandidato', ''), ('inicioFechaPublic', ''), ('finFechaPublic', ''), ('publicada', ''), ('observaciones', ''), ('candidatoSelecc', ''), ('fechaContratacion', ''), ('idRequisicion', ''), ('idPuesto', ''))
        nombres=""
        tipos_dato=()
        for columna in array:
            nombres+=f"{columna[0]},"
            tipos_dato
            tipos_dato+=columna[1],

        nombres=nombres[:-1]
        return nombres,tipos_dato
