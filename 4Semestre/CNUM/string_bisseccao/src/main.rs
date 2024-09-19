mod op;
mod sum_sub;
mod mul_div;
use crate::sum_sub::soma_sub;
use crate::mul_div::mult_div;


fn main() {
    let x = "-2";
    //let mut eq2: String = String::from("$57*x/4.56 + 12*x*12*x*4/3*x + 0*0 - 0*x $");

    
    let mut eq2 = String::from("$x * 2 * 3 * 77 - 3* 99 *5 +23 +56$");


    // Causa  bug
    //-2 * 2 * 3 * 77 - 3* 99 *5 +23 +56
    // 7 * -2
    // -7 * -2 

    
    
    //let eq3 = String::from("$x * 3 + 2$");
    //let eq4 = String::from("$x * (3 + 2)$");

    let mut eqs: String = op::remove_whitespace(&mut eq2); // 9+5-7+5+6-8
    println!("eq inicial: {}", eq2);
    eqs = eqs.replace("x", &x);

    eqs = mult_div(eqs);
    

    println!("\nsoma: {}", eqs);
    soma_sub(eqs);
}