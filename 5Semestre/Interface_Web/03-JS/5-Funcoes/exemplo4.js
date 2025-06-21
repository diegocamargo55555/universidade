function fn(cb){
    console.log('executar funcao de callback')
    console.log(typeof cb)
    cb()
}

function callback() {
    console.log("funcao passada como parametro")
}
fn(callback)



const objeto = {
    nome : "teste", 
    callback
}
objeto.callback()