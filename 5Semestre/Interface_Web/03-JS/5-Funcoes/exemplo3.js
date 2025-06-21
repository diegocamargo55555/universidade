function somar(n1,n2) {
    return n1+ n2
    
}
console.log(somar(1,2))

function somar2(){
    let total = 0 
    for (let i = 0; i < arguments.length; i++) {
        total += arguments[i]
        
    }
    return total
}

console.log(somar2(1,2,4,8))