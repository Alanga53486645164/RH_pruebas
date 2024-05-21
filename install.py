# NOTA: PARA DECLARAR LAS LIBRERIAS A INSTALAR SE NECESITA CREAR UN ARCHIVO TXT LLAMADA:'libs_to_install.txt'
    #parar crear dicho archivo puedes optar por ejecutar este programa una vez, lo creara automaticamente si no lo encuentra.
    #solo seria modificarlo para añadir las librerias a instalar
import subprocess
import os


os.chdir('./')

class Librerias:
    def __init__(self,librerias):
        if(librerias==None or librerias!=""):
            self.librerias=librerias.split(',')
            print(self.librerias)

    def ejecutarComandos(self):
        instaladas=()
        for lib in self.librerias:
            if(self.executeInTerminal(f'pip show {lib}')==-1):
                print('hay que instalar %s'%(lib))
                r=self.executeInTerminal('pip3 install %s'%(lib))
            else:
                r=1
            if r==1:
                instaladas+=lib,
            print(f'{lib} ya instalado')
        
        return instaladas

    def executeInTerminal(self,comando):
        try:
            r=subprocess.run(comando, shell=True, check=True)
            print(f"El comando se ejecutó correctamente:{comando}")
            return 1
        except subprocess.CalledProcessError as e:
            # print(f"Hubo un error al ejecutar el comando: {e}")
            return -1
""" 
flujo de la instalacion:
    1.-existe el archivo de instalados?:
        no:
            -creamos el archivo
            -instalamos las librerias
        si:
            -leemos el archivo de libs a instalar
            -leemos el archivo de instalados
            -son inguales?
                si
                    termina el proceso, ya no hay nadad que hacer
                no
                    -instalamos la libreria


"""

def instalarLibrerias():
    try:
        libs=getLibsForInstall('r')
    except Exception:
        open('libs_to_install.txt','x')
        getLibsForInstall('w').write(getInstallLibsTextDescription())
        print('__termino de escribir la instrucciones')

    print('empezo a leer el libs to install')
    libs=getLibsForInstall('r')
    try:
        open('installed.txt','x')
        print('no hay libs instaladas(se acaba de crear el archivo installed.txt)')
        
        actualizarInstalados(libs)
        # no existe el archivo instalado.txt
    except Exception:
        print('ya existe el acrhivo de instalados')
        #ya existe el archivo instalado
        libs_act=getLibsInstaled('r')

        if len(libs_act.split('(ERROR)')) ==2:
            return
        
        # libs_act=libs_act.split(getInstallLibsTextDescription())[1]

        # libs_act_txt=libs_act.split('sintaxis: nombre_libreria,nombre_libreria2,etc\n-')
        print(f"__{libs}==?{libs_act}")
        if libs!=libs_act:
        # if libs!=libs_act_txt:
            actualizarInstalados(libs)
        print('ya estan instaladas las librerias: %s'%(libs))

def getInstallLibsTextDescription():
    return 'sintaxis(empieza a escribir a partir del "-"): nombre_libreria,nombre_libreria2,etc\n-'

def actualizarInstalados(libs_to_install):
    libreria=Librerias(libs_to_install)
    install=",".join(libreria.ejecutarComandos())
    if(install!=libs_to_install):
        install+="(ERROR)"
    getLibsInstaled('w').write(install)

def getLibsForInstall(accion):
    libs=open("libs_to_install.txt", accion)
    if accion=='r':
        return libs.read().split(getInstallLibsTextDescription())[1]
    return libs

def getLibsInstaled(accion):
    libs=open("installed.txt", accion)
    if accion=='r':
        return libs.read()
        
    return libs


instalarLibrerias()