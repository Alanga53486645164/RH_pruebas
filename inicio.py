from install import *
from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql
from sql_admin import Admin
from colorama import init, Fore, Back, Style
from datetime import date,datetime


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html",inicio=True)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('Notfound.html'), 404

@app.route('/verApariciones:<string:id_curso>')
def verAparicion(id_curso):
    conexion=Admin()
    # query=f"select chp.id_registro, mac.nombre, chp.lugar, chp.inicio, chp.fin, e.nombre from curso_has_aparicion chp join cursos c on c.id_curso=chp.id_curso join trabajadores e on chp.id_encargado=e.idTrabajador join modo_aplicacion_curso mac on mac.id_modo=chp.id_metodo_aplicacion where chp.id_curso={id_curso}"
    query=f"select chp.id_registro, mac.nombre, chp.lugar, c.nombre, chp.inicio, chp.fin, e.NombreTrab from curso_has_aparicion chp join cursos c on c.id_curso=chp.id_curso join trabajadores e on chp.id_encargado=e.idTrabajador join modo_aplicacion_curso mac on mac.id_modo=chp.id_metodo_aplicacion where chp.id_curso={id_curso}"
    conexion.execute(query)
    datos=conexion.getResult()
    print(Back.YELLOW,datos,Back.RESET)
    # query=f"SELECT column_name,data_type FROM information_schema.columns  WHERE table_schema = 'rh3' AND table_name = 'curso_has_aparicion' and column_key !='PRI' order by ordinal_position"
    return render_template('area.html',
            comentarios = datos, puestos_cursos=None,
            titulo='Apariciones',tabla_plural='APARICIONES',male=False,
                borrado=True,
                boolean=(),
                edita=True,
                id=id_curso,
                id_tabla=True,
            columnas=('modo de aplicacion','lugar','curso','inicio','fin','encargado'), num_columnas=6,
            # columnas=('modo de aplicacion','lugar','inicio','fin','encargado'), num_columnas=5,
            acciones=0, n_acc=0)

@app.route('/Instanciar_curso:<int:id_curso>:<string:id_registro>')
def instanciarCurso(id_curso,id_registro):
    conexion=Admin()

    datos=()
    conexion.execute("select * from cursos where id_curso=%s"%(id_curso))
    datos+=conexion.getResult(),

    conexion.getSQLCols("curso_has_aparicion",False)
    datos+=conexion.getResult(),

    conexion.execute("select nombre,id_modo from modo_aplicacion_curso")
    datos+=conexion.getResult(),

    conexion.execute("select NombreTrab,idTrabajador from trabajadores")
    datos+=conexion.getResult(),
    edita=False

    if( id_registro!='NR' and id_registro!='CR'):
        conexion.execute("select id_registro,lugar,inicio,fin,id_encargado,id_metodo_aplicacion  from curso_has_aparicion where id_registro=%s"%(id_registro))
        datos+=conexion.getResult()
        edita=True
        id_registro='NR'

    return render_template("newCurso.html",comentar=datos,edita=edita,redir=id_registro)

@app.route('/ActivarCurso:<int:id_curso>:<string:id_registro>:<string:redireccion>', methods=['POST'])
def activar_curso(id_curso,id_registro,redireccion):
    print(f'{Fore.GREEN}__form recibido')
    Encargado=request.form['Encargado']
    MetAplicacion=request.form['MetAplicacion']
    fecha_inicio=request.form['fecha_inicio']
    fecha_fin=request.form['fecha_fin']
    lugar=request.form['lugar']

    conexion=Admin()

    conexion.execute('select id_modo from modo_aplicacion_curso where nombre="%s"'%(MetAplicacion))
    id_modo=conexion.getResult()[0][0]

    conexion.execute('select idTrabajador from trabajadores where NombreTrab="%s"'%(Encargado))
    id_encargado=conexion.getResult()[0][0]

    if(id_registro!="NR"):
        query="update curso_has_aparicion set id_metodo_aplicacion=%s, lugar='%s', inicio='%s',fin='%s', id_encargado=%s where id_registro=%s"%(id_modo,lugar,fecha_inicio,fecha_fin,id_encargado,id_registro)
        conexion.execute(query)

        return redirect(url_for('verAparicion',id_curso=id_curso))
    # id_metodo_aplicacion,lugar,id_curso,inicio,fin,id_encargado

    conexion.execute('select veces_aparecido from cursos where id_curso=%s'%(id_curso))
    edicion=int(conexion.getResult()[0][0])
    edicion+=1

    tupla=(id_modo,lugar,id_curso,fecha_inicio,fecha_fin,id_encargado,str(edicion))
    print(f'{Back.RED}{tupla}{Back.RESET}')

    query=('insert into curso_has_aparicion(id_metodo_aplicacion,lugar,id_curso,inicio,fin,id_encargado,edicion) values(%s,"%s","%s","%s","%s",%s,%s)'
        %tupla)
    conexion.execute(query)
    conexion.execute("update cursos set veces_aparecido=%s where id_curso=%s "%(edicion,id_curso))

    print(f"{Back.RED}{redireccion}{Back.RESET}")
    if(redireccion=='NR'):
        return redirect(url_for('verAparicion',id_curso=id_curso))

    return redirect(url_for('area',tabla='cursos',condicion='NC'))

@app.route('/catalogosEdita:<string:tabla>:<int:id_campo>')
def editar(tabla,id_campo):
    #como 'tabla' recibe el titulo de la tabla
    conexion=Admin()
    table_name=conexion.titleToTable(tabla)

    if(table_name==None):
        return redirect("/")

    template="area_edi.html"

    id_tabla=conexion.tableToId(table_name)

    conexion.execute(f"select * from {table_name}  where {id_tabla} ={id_campo}")
    dato=conexion.getResult()

    campos= conexion.colsToString(table_name,False)[0].split(',')

    comentar=dato[0]
    # if table_name=="cursos":
    #     template="newCurso.html"
    #     comentar=dato
    return render_template(template, comentar=comentar, campo=campos, tabla=table_name, id_campo=id_campo)

@app.route('/catalogos:<string:tabla>:<string:condicion>')
def area(tabla,condicion):
    conexion=Admin()

    if(conexion.existeTabla(tabla)==None or(tabla=='curso_has_aparicion' and condicion=='NC')):
        return redirect("/")

    permitir_borrado=True
    showId=False
    edita=True

    titulo=conexion.tableToTitle(tabla)
    id=conexion.tableToId(tabla)

    #print(f"titulo={titulo}\nid={id}")
    campos="*"
    join=""
    ci=condicion.upper()
    if(condicion=='NC'):
        condicion=""
    else:
        hoy=date.today()
        print(Back.GREEN,"hoy",hoy)

        if condicion=='Activas':
            edita=False
            condicion=f'"{hoy}" between inicio and fin'

        elif condicion=='Pasadas':
            edita=False
            condicion=f' fin < "{hoy}"'

        elif condicion=='Pendientes':
            condicion=f' inicio > "{hoy}"'
        #el metodo comentado servira una vez que desarrolle una funcion para hacer genocidio de datos
        # join=conexion.makeJoinFor(tabla)
        campos='id_registro, modo_aplicacion_curso.nombre,lugar,cursos.nombre,inicio,fin,trabajadores.NombreTrab,edicion'
        join='JOIN cursos ON curso_has_aparicion.id_curso=cursos.id_curso JOIN modo_aplicacion_curso ON curso_has_aparicion.id_metodo_aplicacion=modo_aplicacion_curso.id_modo JOIN trabajadores ON curso_has_aparicion.id_encargado=trabajadores.idTrabajador'
        condicion="WHERE "+condicion

    query=f"select {campos} from {tabla} {join} {condicion} order by {id} asc"

    conexion.execute(query)
    datos = conexion.getResult()

    plural,male=conexion.tablaPlural(titulo)
    plural=plural.upper()

    titulo_columnas=conexion.getColsNameFor(tabla)
    tipo_datos=conexion.colsToString(tabla,False)[1]

    booleanos=conexion.searchBooleanSQL(tipo_datos)

    n_columnas=len(titulo_columnas)

    n_registros=len(datos)
    puestos_cursos=()
    if(tabla=="cursos"):
        permitir_borrado=True
        titulo_columnas+="Puestos Aplicables",
        for curso in datos:
            conexion.execute(f"select p.nomPuesto from puesto_has_cursos pc join puesto p on pc.id_puesto=p.idPuesto where id_curso={curso[0]}")
            p=conexion.getResult()
            puestos=""
            for puesto in p:
                puestos+=puesto[0]+","
            puestos_cursos+=puestos[:-1],

    return render_template("area.html",
            comentarios = datos, n_registros=n_registros, puestos_cursos=puestos_cursos,
            titulo=titulo,tabla_plural=plural,male=male,
                borrado=permitir_borrado,
                boolean=booleanos,
                edita=edita,
            columnas=titulo_columnas, num_columnas=n_columnas,
            acciones=0, n_acc=0, id_tabla=showId,condicion=ci
            )

@app.route('/EditaCatalogos:<string:tabla>:<int:id_campo>',methods=['POST'])
def area_fedita(tabla,id_campo):
    if request.method == 'POST':
        valor=request.form['valor']

        conexion=Admin()
        campos= conexion.colsToString(tabla,True)[0]
        campos=campos.split(",")
        id_tabla=campos[0]
        otro=campos[1]

        conexion.execute('update %s set %s="%s" where %s=%s'%(tabla,otro,valor,id_tabla,id_campo))

    return redirect(url_for('area',tabla=tabla,condicion='NC'))

@app.route('/catalogoBorrar:<string:titulo>:<string:id>:<string:id_aparicion>')
def area_borrar(titulo,id,id_aparicion):

    conexion=Admin()
    table_name=conexion.titleToTable(titulo)
    id_tabla=conexion.tableToId(table_name)
    print("===========")
    print(Back.RED+id_tabla+Back.RESET)
    print(Back.RED+table_name+Back.RESET)
    conexion.execute('delete from {0} where {1} = {2}'.format(table_name,id_tabla,id))

    if(titulo=='Apariciones'):
        return redirect(url_for('verAparicion',id_curso=id_aparicion ))

    return redirect(url_for('area',tabla=table_name,condicion='NC'))

# @app.route('/area_agregar')
@app.route('/catalogosAgregar:<string:tabla_titulo>:<string:id_campo>')
def area_agregar(tabla_titulo,id_campo):
    # if tabla_titulo=="Curso":
    #     return render_template("cursos_agr.html"

    conexion=Admin()
    nombre_tabla=conexion.titleToTable(tabla_titulo)
    dato,tipo_datos=conexion.colsToString(nombre_tabla,False)

    titulo_columnas=conexion.getColsNameFor(nombre_tabla)
    # titulo_columnas=['descripcion']

    # if(nombre_tabla=="cursos"):
    #     titulo_columnas=['nombre','descripcion','duracion','objetivos de aprendizaje','obligatorio']
    booleanos=conexion.searchBooleanSQL(tipo_datos)


    if id_campo!="%":
        id_campo=int(id_campo)
        id_table=conexion.tableToId("cursos")

        conexion.execute(f"select {dato} from cursos where {id_table}={id_campo}")
        fetch =conexion.getResult()
    else:
        fetch=()
        array=()
        for col in range(len(dato.split(","))):
            array+="",
        fetch+=array,

    if(nombre_tabla=="cursos"):
        conexion.execute("select idPuesto,nomPuesto from puesto order by idPuesto desc")
        # res=conexion.getResult()
        titulo_columnas+="Puestos a los que va dirigido :",
        fetch+=conexion.getResult()

    cant_datos=len(titulo_columnas)
    return render_template("area_agr.html",
        columna=dato,titulo=tabla_titulo
        ,datos=titulo_columnas,boolean=booleanos,cDatos=cant_datos,none=None,
        fetch=fetch,id_campo=id_campo
    )

# @app.route('/cursos_agregar')
# def cursos_agregar():
#     return render_template("cursos_agr.html")

# @app.route('/area_fagrega', methods=['POST'])
@app.route('/catalogoPUSH:<string:title>:<string:id_campo>', methods=['POST'])
def area_fagrega(title,id_campo):
    if request.method != 'POST':
        return

    conexion=Admin()
    table_name=conexion.titleToTable(title)

    columnas,tipos_dato=conexion.colsToString(table_name,False)
    datos =table_name,columnas,

    Nombre_columnas=conexion.getColsNameFor(table_name)
    print(f"{Back.WHITE}{Nombre_columnas}{Back.RESET}")
    print(table_name)

    if(table_name=='cursos'):
        print('PADO')
        Nombre_columnas=Nombre_columnas[:-1]

    print(f"{Back.WHITE}{Nombre_columnas}{Back.RESET}")

    uniones=""

    for col in range(len(Nombre_columnas)):
        column=Nombre_columnas[col]
        datos+=(request.form[column]),

        comilla=conexion.getComillas(tipos_dato[col])
        uniones+=f"{comilla}%s{comilla}"

        if col <len(Nombre_columnas)-1:
            uniones+=","

    if id_campo=="%":
        if(table_name=='cursos'):
            uniones+=",0"

        conexion.execute(f'insert into %s (%s) values ({uniones})'%datos)
    else:
        sets=""
        if(table_name=='cursos'):
            columnas=",".join(columnas.split(',')[:-1])

        for col in columnas.split(","):
            sets+=" %s =replace_ ,"
        sets=sets[:-1]
        # a los '%s' les mandamos el nombre del campo que van a actualizar
        sets=sets%tuple(columnas.split(","))
        #remplazamos 'replace_' para ahora guardar los valores que vamos a enviar
        sets=sets.replace("replace_","%s")

        #a los nuevos %s de la sentencia les damos las comillas si las requieren para enviar el dato respectivo correctamente
        sets=sets%tuple(uniones.split(","))
        #uniomos el layout de sets con los datos a actualizar
        sets=sets%datos[2:]
        id_tabla=conexion.tableToId(table_name)
        query=f"update {table_name} set {sets} where {id_tabla}={id_campo}"
        conexion.execute(query)

    if table_name=="cursos":
        puestos=request.form['puestos']
        puestos=puestos.replace("puesto-","").split("|")[1:]
        conexion.execute("select id_curso from cursos where nombre='%s'"%(datos[2]))
        id_curso=conexion.getResult()[0]

        query="delete from puesto_has_cursos where id_curso=%s"%(id_curso)
        conexion.execute(query)

        values=""
        for puesto in  puestos:
            values+=f"({id_curso[0]},{puesto}),"

        values=values[:-1]
        query=f"insert into puesto_has_cursos(id_curso,id_puesto) values {values}"
        conexion.execute(query)
        # else:
        #     values=""
        #     for puesto in puestos:
        #         values=f"id_puesto={puesto}"
        #         query=f"update puesto_has_curso set {values} where id_curso={id_curso} and id_puesto={puesto}"
        #         conexion.execute(query)
    return redirect(url_for('area',tabla=table_name,condicion='NC'))

# @app.route('/EditaCurso:<int:id_curso>')
# def editaCurso(id_curso):
#     return redirect("")

@app.route('/puesto')
def puesto():

    conexion=Admin()


    conexion.execute('select idPuesto, nomPuesto from puesto order by idPuesto')
    datos = conexion.getResult()

    return render_template("puesto.html", pue = datos, dat='   ', catArea = '   ', catEdoCivil = '   ', catEscolaridad = '   ',
                           catGradoAvance = '    ', catCarrera = '    ', catIdioma = ' ', catHabilidad = ' ')


@app.route('/puesto_fdetalle/<string:idP>', methods=['GET'])
def puesto_fdetalle(idP):

    conexion=Admin()


    conexion.execute('select idPuesto, nomPuesto from puesto order by idPuesto')
    datos = conexion.getResult()

    conexion.execute(f"""select idPuesto,codPuesto,idArea,nomPuesto,puestoJefeSup,jornada,remunMensual,prestaciones,descripcionGeneral,
            funciones,edad,sexo,idEstadoCivil,idEscolaridad,idGradoAvance,idCarrera,experiencia,conocimientos,manejoEquipo,'
            'reqFisicos,reqPsicologicos,responsabilidades,condicionesTrabajo from puesto where idPuesto = {idP}""" )
    dato = conexion.getResult()

    conexion.execute('select a.idArea, a.descripcion from area a, puesto b where a.idArea = b.idArea and b.idPuesto = %s'%(idP))
    datos1 = conexion.getResult()

    conexion.execute('select a.idEstadoCivil, a.descripcion from estado_civil a, puesto b where a.idEstadoCivil = b.idEstadoCivil and b.idPuesto = %s'%(idP))
    datos2 = conexion.getResult()

    conexion.execute('select a.idEscolaridad, a.descripcion from escolaridad a, puesto b where a.idEscolaridad = b.idEscolaridad and b.idPuesto = %s'%(idP))
    datos3 = conexion.getResult()

    conexion.execute('select a.idGradoAvance, a.descripcion from grado_avance a, puesto b where a.idGradoAvance = b.idGradoAvance and b.idPuesto = %s'%(idP))
    datos4 = conexion.getResult()

    conexion.execute('select a.idCarrera, a.descripcion from carrera a, puesto b where a.idCarrera = b.idCarrera and b.idPuesto = %s'%(idP))
    datos5 = conexion.getResult()

    conexion.execute('select a.idPuesto, b.idIdioma, b.descripcion from puesto a, idioma b, puesto_has_idioma c '
                   'where a.idPuesto = c.idPuesto and b.idIdioma = c.idIdioma and a.idPuesto = %s'%(idP))
    datos6 = conexion.getResult()

    conexion.execute(f'select a.idPuesto, b.idHabilidad, b.descripcion from puesto a, habilidad b, puesto_has_habilidad c where a.idPuesto = c.idPuesto and b.idHabilidad = c.idHabilidad and a.idPuesto = {idP}')
    datos7 = conexion.getResult()
    return render_template("puesto.html", pue = datos, dat=dato[0], catArea=datos1[0], catEdoCivil=datos2[0], catEscolaridad=datos3[0],
                           catGradoAvance=datos4[0], catCarrera=datos5[0], catIdioma=datos6, catHabilidad=datos7)

@app.route('/puesto_borrar/<string:idP>')
def puesto_borrar(idP):

    conexion=Admin()

    conexion.execute('delete from puesto where idPuesto = %s'%(idP))

    conexion.execute('delete from puesto_has_habilidad where idPuesto =%s '%(idP))

    conexion.execute('delete from puesto_has_idioma where idPuesto =%s '%(idP))

    return redirect(url_for('puesto'))


@app.route('/puesto_agrOp2')
def puesto_agrOp2():

    conexion=Admin()

    conexion.execute('select idArea, descripcion from area ')
    datos1 = conexion.getResult()

    conexion.execute('select idEstadoCivil, descripcion from estado_civil ')
    datos2 = conexion.getResult()

    conexion.execute('select idEscolaridad, descripcion from escolaridad ')
    datos3 = conexion.getResult()

    conexion.execute('select idGradoAvance, descripcion from grado_avance ')
    datos4 = conexion.getResult()

    conexion.execute('select idCarrera, descripcion from carrera ')
    datos5 = conexion.getResult()

    conexion.execute('select idIdioma, descripcion from idioma ')
    datos6 = conexion.getResult()

    conexion.execute('select idHabilidad, descripcion from habilidad ')
    datos7 = conexion.getResult()

    return render_template("puesto_agrOp2.html", catArea=datos1, catEdoCivil=datos2, catEscolaridad=datos3,
                           catGradoAvance=datos4, catCarrera=datos5, catIdioma=datos6, catHabilidad=datos7)


@app.route('/puesto_fagrega2', methods=['POST'])
def puesto_fagrega():
    if request.method == 'POST':

        if  'idArea' in request.form:
            idAr = request.form['idArea']
        else:
            idAr = '1'
        if 'idEstadoCivil' in request.form:
            idEC = request.form['idEstadoCivil']
        else:
            idEC = '1'
        if 'idEscolaridad' in request.form:
            idEs = request.form['idEscolaridad']
        else:
            idEs = '1'
        if 'idGradoAvance' in request.form:
            idGA = request.form['idGradoAvance']
        else:
            idGA = '1'
        if 'idCarrera' in request.form:
            idCa = request.form['idCarrera']
        else:
            idCa = '1'
        if 'sexo' in request.form:
            sex = request.form['sexo']
        else:
            sex = '1'
        codP = request.form['codPuesto']
        nomP = request.form['nomPuesto']
        pueJ = request.form['puestoJefeSup']
        jorn = request.form['jornada']
        remu = request.form['remunMensual']
        pres = request.form['prestaciones']
        desc = request.form['descripcionGeneral']
        func = request.form['funciones']
        eda = request.form['edad']
        expe = request.form['experiencia']
        cono = request.form['conocimientos']
        manE = request.form['manejoEquipo']
        reqF = request.form['reqFisicos']
        reqP = request.form['reqPsicologicos']
        resp = request.form['responsabilidades']
        conT = request.form['condicionesTrabajo']



    conexion=Admin()

    conexion.execute(
    """insert into puesto (codPuesto,idArea,nomPuesto,puestoJefeSup,jornada,remunMensual,prestaciones,descripcionGeneral,
    funciones,edad,sexo,idEstadoCivil,idEscolaridad,idGradoAvance,idCarrera,experiencia,conocimientos,manejoEquipo,
    reqFisicos,reqPsicologicos,responsabilidades,condicionesTrabajo) values (%s,'%s',%s,'%s','%s','%s',%s,'%s','%s','%s','%s','%s',%s,%s,%s,%s,'%s','%s','%s','%s','%s','%s')"""%
    (codP, idAr, nomP, pueJ, jorn, remu, pres, desc, func, eda, sex, idEC, idEs, idGA, idCa, expe, cono, manE, reqF,
     reqP, resp, conT))


    conexion.execute('select idPuesto from puesto where idPuesto=(select max(idPuesto) from puesto) ')
    dato = conexion.getResult()
    idpue = dato[0]
    idP = idpue[0]

    conexion.execute('select count(*) from idioma ')
    dato = conexion.getResult()
    nidio = dato[0]
    ni = nidio[0] + 1

    for i in range(1, ni):
        idio = 'i' + str(i)
        if idio in request.form:
            conexion.execute('insert into puesto_has_idioma(idPuesto,idIdioma) values (%s,"%s")'%(idP, i))


    conexion.execute('select count(*) from habilidad ')
    dato = conexion.getResult()
    nhab = dato[0]
    nh =nhab[0]+1

    for i in range(1,nh):
        habi = 'h' + str(i)
        if habi in request.form:
            conexion.execute('insert into puesto_has_habilidad(idPuesto,idHabilidad) values (%s,%s)'%(idP,i))


    return redirect(url_for('puesto'))



@app.route('/puesto_editar/<string:idP>')
def puesto_editar(idP):

    conexion=Admin()


    conexion.execute('select idPuesto,codPuesto,idArea,nomPuesto,puestoJefeSup,jornada,remunMensual,prestaciones,descripcionGeneral,'
        'funciones,edad,sexo,idEstadoCivil,idEscolaridad,idGradoAvance,idCarrera,experiencia,conocimientos,manejoEquipo,'
        'reqFisicos,reqPsicologicos,responsabilidades,condicionesTrabajo from puesto where idPuesto = %s'%(idP))
    dato = conexion.getResult()

    conexion.execute('select idArea, descripcion from area ')
    datos1 = conexion.getResult()

    conexion.execute('select idEstadoCivil, descripcion from estado_civil ')
    datos2 = conexion.getResult()

    conexion.execute('select idEscolaridad, descripcion from escolaridad ')
    datos3 = conexion.getResult()

    conexion.execute('select idGradoAvance, descripcion from grado_avance ')
    datos4 = conexion.getResult()

    conexion.execute('select idCarrera, descripcion from carrera ')
    datos5 = conexion.getResult()

    conexion.execute('select idIdioma, descripcion from idioma ')
    datos6 = conexion.getResult()

    conexion.execute('select idHabilidad, descripcion from habilidad ')
    datos7 = conexion.getResult()

    conexion.execute('select a.idArea, a.descripcion from area a, puesto b where a.idArea = b.idArea and b.idPuesto = %s'%(idP))
    datos11 = conexion.getResult()

    conexion.execute('select a.idEstadoCivil, a.descripcion from estado_civil a, puesto b where a.idEstadoCivil = b.idEstadoCivil and b.idPuesto = %s'%(idP))
    datos12 = conexion.getResult()

    conexion.execute('select a.idEscolaridad, a.descripcion from escolaridad a, puesto b where a.idEscolaridad = b.idEscolaridad and b.idPuesto = %s'%(idP))
    datos13 = conexion.getResult()

    conexion.execute('select a.idGradoAvance, a.descripcion from grado_avance a, puesto b where a.idGradoAvance = b.idGradoAvance and b.idPuesto = %s'%(idP))
    datos14 = conexion.getResult()

    conexion.execute('select a.idCarrera, a.descripcion from carrera a, puesto b where a.idCarrera = b.idCarrera and b.idPuesto = %s'%(idP))
    datos15 = conexion.getResult()

    conexion.execute('select a.idPuesto, b.idIdioma, b.descripcion from puesto a, idioma b, puesto_has_idioma c '
                   'where a.idPuesto = c.idPuesto and b.idIdioma = c.idIdioma and a.idPuesto = %s'%(idP))
    datos16 = conexion.getResult()

    conexion.execute('select a.idPuesto, b.idHabilidad, b.descripcion from puesto a, habilidad b, puesto_has_habilidad c '
                   'where a.idPuesto = c.idPuesto and b.idHabilidad = c.idHabilidad and a.idPuesto = %s'%(idP))
    datos17 = conexion.getResult()


    return render_template("puesto_edi.html", dat=dato[0], catArea=datos1, catEdoCivil=datos2, catEscolaridad=datos3,
                           catGradoAvance=datos4, catCarrera=datos5, catIdioma=datos6, catHabilidad=datos7,
                           Area=datos11[0], EdoCivil=datos12[0], Escolaridad=datos13[0], GradoAvance=datos14[0],
                           Carrera=datos15[0], Idioma=datos16, Habilidad=datos17)


@app.route('/puesto_fedita/<string:idP>', methods=['POST'])
def puesto_fedita(idP):
    if request.method == 'POST':
        codP = request.form['codPuesto']
        idAr = request.form['idArea']
        nomP = request.form['nomPuesto']
        pueJ = request.form['puestoJefeSup']
        jorn = request.form['jornada']
        remu = request.form['remunMensual']
        pres = request.form['prestaciones']
        desc = request.form['descripcionGeneral']
        func = request.form['funciones']
        eda = request.form['edad']
        sex = request.form['sexo']
        idEC = request.form['idEstadoCivil']
        idEs = request.form['idEscolaridad']
        idGA = request.form['idGradoAvance']
        idCa = request.form['idCarrera']
        expe = request.form['experiencia']
        cono = request.form['conocimientos']
        manE = request.form['manejoEquipo']
        reqF = request.form['reqFisicos']
        reqP = request.form['reqPsicologicos']
        resp = request.form['responsabilidades']
        conT = request.form['condicionesTrabajo']


    conexion=Admin()


    conexion.execute("""update puesto set codPuesto = '%s', idArea = %s, nomPuesto = '%s', puestoJefeSup = '%s', jornada = '%s',
                  remunMensual = %s, prestaciones = '%s', descripcionGeneral = '%s', funciones = '%s', edad = '%s', sexo = '%s',
                  idEstadoCivil = %s, idEscolaridad = %s, idGradoAvance = %s, idCarrera = %s, experiencia = '%s',
                  conocimientos = '%s', manejoEquipo = '%s', reqFisicos = '%s', reqPsicologicos = '%s', responsabilidades = '%s',
                  condicionesTrabajo = '%s' where idPuesto = %s"""%(codP, idAr, nomP, pueJ, jorn, remu, pres, desc, func, eda,
                   sex, idEC, idEs, idGA, idCa, expe, cono, manE, reqF, reqP, resp, conT, idP))


    conexion.execute('delete from puesto_has_habilidad where idPuesto =%s '%(idP))

    conexion.execute('delete from puesto_has_idioma where idPuesto =%s '%(idP))


    conexion.execute('select count(*) from idioma ')
    dato = conexion.getResult()
    nidio = dato[0]
    ni = nidio[0] + 1

    for i in range(1, ni):
        idio = 'i' + str(i)
        if idio in request.form:
            conexion.execute('insert into puesto_has_idioma(idPuesto,idIdioma) values (%s,"%s")'%(idP, i))


    conexion.execute('select count(*) from habilidad ')
    dato = conexion.getResult()
    nhab = dato[0]
    nh = nhab[0] + 1

    for i in range(1, nh):
        habi = 'h' + str(i)
        if habi in request.form:
            conexion.execute('insert into puesto_has_habilidad(idPuesto,idHabilidad) values (%s,"%s")'%(idP, i))

    return redirect(url_for('puesto'))




if __name__ == "__main__":
    app.run(debug=True
        ,port=5001
    )
