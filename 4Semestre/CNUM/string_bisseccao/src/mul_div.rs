use crate::op::remove_whitespace;
use crate::op::prep_troca;

pub fn posi_mult_div(eqs: String) -> Vec<usize>{
    let (mut mult2, mut div2, cifrao) = (98,98, 0);
    let (mult,  div);
    let cifrao2: usize = eqs.len() - 1; // pega a ultima posição do vetor


    mult = eqs.chars().position(|c| c == '*').unwrap_or(99);
    if mult != 99 {
        mult2 = eqs[mult + 1..].chars().position(|c| c == '*').unwrap_or(99)+ mult + 1;
    }

    div = eqs.chars().position(|c| c == '/').unwrap_or(99);
    if div != 99 {
        div2 = eqs[div + 1..].chars().position(|c| c == '*').unwrap_or(99)+ div + 1;
    }

    let mut v: Vec<usize> = vec![cifrao, mult, mult2,  div, div2, cifrao2];
    v.sort();

    return v;
}

pub fn mult_div(mut eqs: String) ->String{
    let mut resultado_str;
    let mut repet = eqs.chars().filter(|c| *c == '*').count();
    repet += eqs.chars().filter(|c| *c == '/').count();


    for _i in 0..repet {
        eqs = remove_whitespace(&mut eqs); 

        println!("--------\ninicio: {}", eqs);

        let mut v = posi_mult_div(eqs.clone());
        println!("vetor{:?}", v);

        if &eqs[1..2] == "-" {

            resultado_str = prep_troca(eqs.clone(), &v);
            println!("antes: {}", eqs);
             
            eqs.replace_range(v[2] + 1..v[3] , &resultado_str); // troca os chars entre o terceiro e quarto sinal pelo resulado 
            v = posi_mult_div(eqs.clone());
            eqs.replace_range(v[1]..v[2] + 1, " "); //
        } 
        else {

            resultado_str = prep_troca(eqs.clone(), &v);

            eqs.replace_range(v[1] + 1..v[2] , &resultado_str); //

            v = posi_mult_div(eqs.clone());
            eqs.replace_range(v[0] + 1..v[1] + 1, " "); //
        }
        println!("fim: {}", eqs);
    }

    return eqs;
}