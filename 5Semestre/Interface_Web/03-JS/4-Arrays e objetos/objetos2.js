let valor = {n: 10}
let valor2 = {n: 10}

function mudaValor(obj) {
    obj.n++
    console.log("valor interno", obj.n);
}

mudaValor(valor)
console.log("valor externo", valor);

console.log(valor === valor2);
