let colapsar=document.getElementById('colaps')
let lateral,tablas
function colapsarLateral(){
    lateral=document.getElementsByClassName('barra-lateral')[0]
    tablas=document.getElementsByTagName('main')[0]
    if (lateral.checkVisibility()){
        lateral.style.display='None'
        tablas.style.marginLeft='0px'
        colapsar.style.left='0px'
    }else{
        lateral.style.display=''
        tablas.style.marginLeft=''
        colapsar.style.left=''
    }
}
colapsar.onclick=function (){
    console.log('clicked');   
    colapsarLateral()
}
function LimpiarEntreTiempoTecleado(){
    setTimeout(function (){
        window.anterior=null
    },500)
}
let target
window.addEventListener('keydown',function(e){
// document.getElementsByTagName('body')[0].addEventListener('keydown',function(e){
    target=e
    LimpiarEntreTiempoTecleado()
    if(this.anterior==null){
        this.anterior=e.key
        return
    }
    if(this.anterior!='b' && this.anterior!='Control'){
        return
    }
    if(e.key!='b' && e.key!='Control'){
        return
    }
    if(e.key==this.anterior){
        this.anterior=null
        return
    }
    this.anterior=null
    colapsarLateral()
    console.log(e.key);
})