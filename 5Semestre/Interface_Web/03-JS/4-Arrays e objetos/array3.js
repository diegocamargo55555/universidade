const arr = [1, 5, 10, "ola", true]

let sohNumeros = arr.some(function(el){
    return typeof el === "number" //checa se tem pelo menos um numero
})

console.log(sohNumeros)