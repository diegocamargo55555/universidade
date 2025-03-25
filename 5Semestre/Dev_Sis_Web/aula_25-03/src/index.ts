const disciplina : string = "desenvolvimento de sistemas web"

console.log(disciplina)

var a = 6 
var b = 15
if (a === 6){
    let a = 5 // este mantem o resultado interno ao bloco
    var b = 3 // este sai do bloco
    console.log(a) // = 5
    console.log(b) // = 3
    var b = 5
}
console.log(a) // = 6
console.log(b) // = 3


function minhaFuncao(n1: number, n2: number): number {
    console.log("minha Função");
    return n1+n2
    
}
console.log("O resultado é " + minhaFuncao(5,4))