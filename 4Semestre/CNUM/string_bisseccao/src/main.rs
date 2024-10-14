mod op;
mod sum_sub;
mod mul_div;
use op::do_eq;

use crate::sum_sub::soma_sub;
use crate::mul_div::mult_div;
mod exp;
use crate::exp::exp_main;

//use crate::exp::expo;


fn main() {
    let x = "-2";
    //let mut eq2: String = String::from("$55*-3 $");

    
    //let mut eq2 = String::from("$x * 2 * 3 / 77 - 3* 99 *5 +23 +5$");
    //let mut eq2 = String::from("$78 +54 -99 - 55 -45 +15 $");
    
    
    let mut eq2 = String::from("$-9^2 +2/3$");
    //let eq4 = String::from("$x * (3 + 2)$");

    let mut eqs: String = op::remove_whitespace(&mut eq2); // 9+5-7+5+6-8
    println!("eq inicial: {}", eq2);
    eqs = eqs.replace("x", &x);





    let p_ini = eqs.rfind('(').unwrap_or(99);
    let p_fim =eqs.chars().position(|c| c == ')').unwrap_or(99);    

    let mut temp_eq = eqs[p_ini+1..p_fim].to_string();

    

     if p_ini == 99 {
        let result  = do_eq(eqs.to_string());
    }else {
        let mut temp_eq = eqs[p_ini+1..p_fim].to_string();
        temp_eq.insert(p_fim-p_ini-1, '$');// (45)
        temp_eq.insert(0, '$');

        let result  = do_eq(temp_eq).replace('$', "");


        eqs.replace_range(p_ini..p_fim+1, &result);

        println!("fim: {}",eqs)
    }


/*     eqs = exp_main(eqs);
    println!("\nEXP: {}", eqs);

    eqs = mult_div(eqs);

    println!("\nsoma: {}", eqs);
    soma_sub(eqs);
 */    
}