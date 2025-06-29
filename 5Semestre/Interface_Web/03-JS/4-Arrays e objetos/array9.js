const arr = [1, 2, 3]
show(1,2,3)
show(arr)
show(...arr)

function show(){
    console.log(arguments);
    console.log(arguments.length);
    
    
}

let[n1] = arr
console.log(n1);
let[n2,n3] = arr
console.log(n2);
console.log(n3);

