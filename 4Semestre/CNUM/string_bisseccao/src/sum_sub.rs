use crate::op::prep_troca;
use crate::op::remove_whitespace;
use crate::op::posi_sum_sub;

pub fn soma_sub(mut eqs: String) {
    
    let mut resultado_str;
    let mut repet = eqs.chars().filter(|c| *c == '-').count();
    repet += eqs.chars().filter(|c| *c == '+').count();


    for _ in 0..repet {
        eqs = remove_whitespace(&mut eqs); 
        println!("--------\ninicio: {}", eqs);

        let mut v = posi_sum_sub(eqs.clone()); // pega a posição em que está o sinal e ordena em ordem crescente 
        println!("vetor{:?}", v);

        if &eqs[1..2] == "-" {

            resultado_str = prep_troca(eqs.clone(), &v);
            println!("antes: {}", eqs);
             
            eqs.replace_range(v[2] + 1..v[3] , &resultado_str); // troca os chars entre o terceiro e quarto sinal pelo resulado 
            v = posi_sum_sub(eqs.clone());
            eqs.replace_range(v[1]..v[2] + 1, " "); //
        } 
        else {

            resultado_str = prep_troca(eqs.clone(), &v);
            println!("antes: {}", eqs);

            eqs.replace_range(v[1] + 1..v[2] , &resultado_str); //
            v = posi_sum_sub(eqs.clone());
            eqs.replace_range(v[0] + 1..v[1] + 1, " "); // 
        }
        println!("fim: {}", eqs);
    }
}
