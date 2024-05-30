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
 
    def LastIncomplete(self):
        if self.bloque[-1:]!="":
            #el ultimo split del texto esta lleno, es decir, el bloque no termino en ';'.Por ende,
                #tomo la mitad de una intruccion que continuara en el siguiente bloque
            self.primera_mitad=self.bloque[-1:][0]
            self.bloque=self.bloque[:-1]
            return 1
        #todas las instrucciones estan completas
        self.primera_mitad=None
        return -1

    def esPuntoYComa(self,bloque):
        return (len(bloque)==2  and bloque[0].replace(' ','')=='' and bloque[1].replace(' ','')=='')
    
    def isMidInstruccion(self):
        return (self.primera_mitad!=None)
    
    def unirInstruccion(self):
        if self.esPuntoYComa(self.bloque) or self.isMidInstruccion() ==False:
            #solo se tomo un misero ';'
                            # O
            #en el bucle pasado no hubo instruccion incompleta al final
            #no hay necesidad de unir
                # (condicionales en order de acuerdo a lo aqui dicho)
            return -1
        
        if len(self.bloque)==1:
            #el bucle pasado tomo la mitad de una instruccion
            #   y el actual tomo otra parte, pero no la final
            self.primera_mitad+=self.bloque[0]
            return 1
        
        #bucle pasado tomo la primer mitad de una intruccion
        #   eso significa que ya tenemos la instruccion completa
        #hay que unir ambas partes
        if self.bloque[0]=='':
            # emplieza el bloque con un ';', seguido de una instruccion, tal vez incompleta.Eso se vera en la siguiente fase
            self.bloque[0]=self.primera_mitad
            return 2
        #empieza el bloque con una instruccion, pueden ser varias
        self.bloque[0]= self.primera_mitad+self.bloque[0]
        #unidas
        return 3
        

    def getSQLines(self,archivo): 
        #quitamos los espacios en blanco de mas
        self.bloque= archivo.read(3500).replace('  ',' ')
        print(self.bloque)
        #separamos por lineas sql
        self.bloque=self.bloque.split(";") 
        # escenarios:

        # instruccion incompleta:
        #   primera_mitad!=None

        # medio o inicio
        #   ['abc']
        # fin
        #   ['abc','']
        # varias:
        #     ['abd','sads','']
        
        self.unirInstruccion()

        self.LastIncomplete()
        return self.bloque

        