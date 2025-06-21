function calcularIMC(peso, altura, callback) {
    if (peso === undefined || altura === undefined) {
        throw Error("valores invalidos")
    }
    let imc = peso / (altura * altura)
    if (typeof callback === 'function') {
        return callback(imc)
    }
    return imc
}

function classificaIMC(imc) {
    if (imc <= 16.9) return 'imc muito baixo'
    else if (imc <= 18.4) return "imc baixo"
    else if (imc <= 24.9) return "normal"
    else if (imc <= 29.9) return "acima do peso"
    else if (imc <= 34.9) return "obesidade grau 1"
    else if (imc <= 40) return "obesidade grau 2"
    else return 'obesidade grau 3'
}

let imc = calcularIMC(60, 1.65)
console.log(imc)
console.log("------------------")

let imc2 = (classificaIMC(calcularIMC(60, 1.65, classificaIMC)))
console.log(imc2)