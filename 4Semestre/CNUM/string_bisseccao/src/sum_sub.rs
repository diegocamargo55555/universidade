use crate::op::do_sum_sub;
use crate::op::remove_whitespace;

pub fn soma_sub(mut eqs: String) {
    
    let mut repet = eqs.chars().filter(|c| *c == '-').count();
    repet += eqs.chars().filter(|c| *c == '+').count();


    for _ in 0..repet {
        eqs = remove_whitespace(&mut eqs); 
        println!("--------\ninicio: {}", eqs);

        let v = posi_sum_sub(eqs.clone()); // pega a posição em que está o sinal e ordena em ordem crescente 
        println!("vetor{:?}", v);

        eqs = do_sum_sub(eqs.clone(), &v);

        println!("fim: {}", eqs);
    }
}


pub fn posi_sum_sub(eqs: String) -> Vec<usize> { // pega a posição em que está o sinal e ordena em ordem crescente 
let (mut menos2, mut mais2, cifrao) = (98, 98, 0);
    let (menos, mais);
    let cifrao2: usize = eqs.len() - 1; // pega a ultima posição do vetor

    menos = eqs.chars().position(|c| c == '-').unwrap_or(99);
    if menos != 99 {
        menos2 = eqs[menos + 1..].chars().position(|c| c == '-').unwrap_or(99)+ menos + 1;
    }

    mais = eqs.chars().position(|c| c == '+').unwrap_or(99);
    if mais != 99 {
        mais2 = eqs[mais + 1..].chars().position(|c| c == '+').unwrap_or(99) + mais + 1;
    }

    let mut v: Vec<usize> = vec![cifrao, menos, menos2, mais, mais2, cifrao2];
    v.sort();

    return v;
}