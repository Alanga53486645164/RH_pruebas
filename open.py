from colorama import Fore,Back
#   POSIBLES ESCENARIOS

#>>> 'unidos; asdaas;asdsad'.split(";")
#['unidos', ' asdaas', 'asdsad']

#>>> 'unidos; asdaas;asdsad;'.split(";")
#['unidos', ' asdaas', 'asdsad', '']

#>>> '123333 nknk1j2 bc1k c '.split(';')
#['123333 nknk1j2 bc1k c ']

# bloque=[]
# bloque+='12341'
# bloque
# ['1', '2', '3', '4', '1']
# bloque+='12341',
# bloque
# ['1', '2', '3', '4', '1', '12341']


class SQLFile(): 
    # principal problematica a resolver: tomar instrucciones incompletas que cotinuan en el siguiente bloque de read()
    #debo separar por ';'
    # asi como almacear las pars incompletad y unirlas cuando se complete la instrccion
    primera_mitad=None
    bloque=None

    def media_instruccion(self):
        #separamos por lineas sql
        bloque=self.bloque.split(";") 
        # escenarios:

        # instruccion incompleta:
        #   primera_mitad!=None

        # medio o inicio
        #   ['abc']
        # fin
        #   ['abc','']
        # varias:
        #     ['abd','sads','']
        
        if self.isPrimera_mitad() ==1:
            self.primera_mitad=bloque[len(bloque)-1]

        if self.primera_mitad!=None:
            #bucle pasado tomo la primer mitad de una intruccion
            #hay que unir ambas partes
            bloque[0]=self.primera_mitad+bloque[0]
            #unidas

        if len(bloque) >1:
            #tomaste mas de una instruccion
            self.bloques+=bloque,
        else:
            #tomamos la parte media de una instruccion
        
            self.bloques+=bloque,
        
            self.bloques[len(self.bloques)]=bloque[0]

                
    def isPrimera_mitad(self,bloque):
        if bloque[-1:]!="":
            #el ultimo split del texto esta lleno, es decir, el bloque no termino en ';'.Por ende,
                #tomo la mitad de una intruccion que continuara en el siguiente bloque
            return 1
        else:
            #todas las instrucciones estan completas
            self.primera_mitad=None
            return -1

    def getSQLines(self,archivo): 
        #quitamos los saltos de linea
        self.bloque= archivo.read(3500).replace('\n','')
        print(self.bloque)

        #el bucle pasado tomo una instruccion incompleta
        self.mitad_faltante()

        #el bucle actual tomo el centro de una instruccion
        self.media_instruccion()

        #el bucle tomo la primer mitad de una instruccion
        self.primera_mitad()
        