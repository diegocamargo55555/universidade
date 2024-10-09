mod op;
mod sum_sub;
mod mul_div;
use crate::sum_sub::soma_sub;
use crate::mul_div::mult_div;
//use crate::exp::expo;


fn main() {
    let x = "-2";
    //let mut eq2: String = String::from("$55*-3 $");

    
    let mut eq2 = String::from("$x * 2 * 3 / 77 - 3* 99 *5 +23 +5$"); // causa bug 23 +x (x = -2)
    //let mut eq2 = String::from("$78 +54 -99 - 55 -45 +15 $");
    
    
    //let eq3 = String::from("$x * 3 + 2$");
    //let eq4 = String::from("$x * (3 + 2)$");

    let mut eqs: String = op::remove_whitespace(&mut eq2); // 9+5-7+5+6-8
    println!("eq inicial: {}", eq2);
    eqs = eqs.replace("x", &x);


    //eqs = exp(eqs);
    eqs = mult_div(eqs);
    

    println!("\nsoma: {}", eqs);
    soma_sub(eqs);
}