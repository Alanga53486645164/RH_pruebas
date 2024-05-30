function mostrarDetalles(event, id, nombre, codigo, area, puestoJefeSup, jornada, remunMensual, prestaciones, descripcionGeneral, funciones, edad, sexo, estadoCivil, escolaridad, gradoAvance, carrera, experiencia, conocimientos, manejoEquipo, reqFisicos, reqPsicologicos, responsabilidades, condicionesTrabajo) {
    event.preventDefault(); 
    document.getElementById('nomPuesto').value = nombre;
    document.getElementById('codPuesto').value = codigo;
    document.getElementById('idArea').value = area;
    document.getElementById('puestoJefeSup').value = puestoJefeSup;
    document.getElementById('jornada').value = jornada;
    document.getElementById('remunMensual').value = remunMensual;
    document.getElementById('prestaciones').value = prestaciones;
    document.getElementById('descripcionGeneral').value = descripcionGeneral;
    document.getElementById('funciones').value = funciones;
    document.getElementById('edad').value = edad;
    document.getElementById('sexo').value = sexo;
    document.getElementById('idEstadoCivil').value = estadoCivil;
    document.getElementById('idEscolaridad').value = escolaridad;
    document.getElementById('idGradoAvance').value = gradoAvance;
    document.getElementById('idCarrera').value = carrera;
    document.getElementById('experiencia').value = experiencia;
    document.getElementById('conocimientos').value = conocimientos;
    document.getElementById('manejoEquipo').value = manejoEquipo;
    document.getElementById('reqFisicos').value = reqFisicos;
    document.getElementById('reqPsicologicos').value = reqPsicologicos;
    document.getElementById('responsabilidades').value = responsabilidades;
    document.getElementById('condicionesTrabajo').value = condicionesTrabajo;
    document.getElementById('detalles').style.display = 'block';
}