from colorama import Fore,Back
#   POSIBLES ESCENARIOS

#>>> 'unidos; asdaas;asdsad'.split(";")
#['unidos', ' asdaas', 'asdsad']

#>>> 'unidos; asdaas;asdsad;'.split(";")
#['unidos', ' asdaas', 'asdsad', '']

#>>> '123333 nknk1j2 bc1k c '.split(';')
#['123333 nknk1j2 bc1k c ']

class SQLFile():
    bloques=[]
    primera_mitad=None
    bloque=None
    
    def mitad_faltante(self):
        if self.primera_mitad!=None:
            self.bloque=self.primera_mitad+self.bloque

            
    def media_instruccion(self):
        bloque=bloque.split(";")
        if len(self.bloques)==0:
            self.bloques+=bloque,
        elif len(bloque)==1:
            self.bloques[len(self.bloques)]=bloque[0]

                
    def primera_mitad(self):
        if self.bloques[len(self.bloques)-1]!="":
            self.primera_mitad=self.bloques[len(self.bloques)-1]
        else:
            self.primera_mitad=None

    def getSQLFile(self):
        with open("rh3Unido.sql", "r",encoding="utf-8") as archivo:
            while True:
                self.bloque= archivo.read(3500)
                print(self.bloque)

                #el bucle pasado tomo una instruccion incompleta
                self.mitad_faltante()

                #el bucle actual tomo el centro de una instruccion
                self.media_instruccion()

                #el bucle tomo la primer mitad de una instruccion
                self.primera_mitad()
                
                print("P____________ESPACIO_____________*")
                if not self.bloque:
                    break

