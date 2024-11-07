fn organiza(v: &mut Vec<i32>, n: usize, i:usize){
    if i > 0 {
        let pai = ((i-1) / 2) as usize;
        let temp ;
    
        if v[pai] > 0 {
            if v[i]> v[pai]{
                temp = v[i];
                v[i] = v[pai];
                v[pai] = temp;
                organiza(v, n, pai)
            }
        }
    }
}

fn insere(v: &mut Vec<i32>, valor: i32){
    v.push(valor);
    let n = v.len();
    organiza(v, n, n-1);
}


fn main() { // 8, 1 , 19 ,7, 73, 35
    let mut v = vec![];

    insere(&mut v, 8);
    insere(&mut v, 1);
    insere(&mut v, 19);
    insere(&mut v, 7);
    insere(&mut v, 73);
    insere(&mut v, 35);

    println!("v:{:?}", v);
}
