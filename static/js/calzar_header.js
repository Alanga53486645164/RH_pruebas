let header=document.getElementById('header')
let target='void'
document.body.onresize=function (){
    // console.error('cambio el header')
    cambiarTamaño(document.body)
    // console.log();
}

function cambiarTamaño(target){
    header=document.getElementById('header')
    target.style.marginTop=header.clientHeight+"px"
}
function iniciarResize(){
    
    let body=document.getElementsByTagName('body')[0]
    cambiarTamaño(body)
}
iniciarResize()