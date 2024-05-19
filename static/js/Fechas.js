class Fecha{
    constructor(fecha_string) {
        let date=fecha_string.split("-")

        if(fecha_string.length!=10 || date.length!=3 || date[0].length!=4 || date[1].length!=2){
            // creo que no necesita el ultimo de :  date[1].length!=2
            return null
        }
        this.year=date[0]
        this.month=date[1]
        this.day=date[2]
    }
    getYear(){
        return parseInt( this.year)
    }
    getMonth(){
        return parseInt( this.month)
    }
    getDay(){
        return parseInt( this.day)
    }
    getDate(){
        return ""+this.getYear()+"-"+this.getMonth()+"-"+this.getDay()
    }
    isBoforeThan(otra_fecha){
        if(otra_fecha.getYear==undefined){
            // no es un objeto de la clase 'Fecha'
            otra_fecha= new Fecha(otra_fecha)
            if(otra_fecha==null){
                return null
            } 
        }
        console.log(otra_fecha.getYear()+"=="+this.getYear());
        if(otra_fecha.getYear()==this.getYear()){
            console.error('mismo AÑO IF');
        }
        if (otra_fecha.getYear()<this.getYear()){
            // el otro año es menor
            console.error("Somos el año MAyor");
            return false
        }
        
        if (otra_fecha.getYear()>this.getYear){
            console.error("Somos el año menor");
            
            // el otro año es mayor
            return true
        }
        console.error("Mismo año")
        // estamos en el mismo año
        if(otra_fecha.getMonth()<this.getMonth()){
            // el otro es antes que nosotros
            return false
        }
        
        if(otra_fecha.getMonth()>this.getMonth()){
            // el otro es depsues de nosotros
            return true
        }
        console.error("Mismo mes")
        //estamos en el mismo mes
        console.error(otra_fecha.getDay(),"<=",this.getDay());
        if(otra_fecha.getDay()<=this.getDay()){
            // el otro dia esta antes de nosotros
            return false
        } 
        console.error("Somos fecha menor")
        //somos la fecha menor
        return true
    }
}
function FechaMasLejana(Fecha1,Fecha2){
    date1=new Fecha(Fecha1)
    date2=new Fecha(Fecha2)
    
    if(date1.isBoforeThan(date2)){
        console.log("Fecha 1(",date1.getDate(),") es menor")
        return 1
    }
    console.log("Fecha 2(",date2.getDate(),") es menor")
    return 2
}

function InicioMenorQue() {
    // let padre = e.target.parentNode;
    
    // if(FechaMasLejana(inicio.value, fin.value)===2){
    //     // boton.validity.valid=false
    //     alert("La fecha de fin debe ser mayor a la fecha de inicio")
    //     return -1
    // }
    if (inicio.value>fin.value){
        alert('La fecha de fin debe ser mayor a la de inicio')
        return -1
    }
    // boton.validity.valid=true
    return 1
}
// FechaMasLejana('2024-02-12','2024-02-12')
let inicio = document.getElementsByName("fecha_inicio")[0]
    let fin = document.getElementsByName("fecha_fin")[0]

    // fin.addEventListener('change', InicioMenorQue);

    let boton=document.getElementsByName("Enviar")[0]
    let padre=document.getElementsByTagName("form")[0]
    
    padre.addEventListener("submit",function enviar(e){
        // alert('SUBMIT')
        if (InicioMenorQue()===-1){ 
            // alert('PREVENT')
            e.preventDefault()
            return
        }
        // alert('SE DEBE ENVIAR')
        // let selects=document.getElementsByTagName('select')
        // for(index=0;index<selects.length;index++){
        //     let targetName= selects[index].getAttribute('data-targetName')
        //     let target= document.getElementsByName(targetName)

        // }
    })

    // let selects= document.getElementsByTagName("select")