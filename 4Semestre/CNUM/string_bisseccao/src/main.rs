mod op;
mod sum_sub;
mod mul_div;
use crate::sum_sub::soma_sub;
use crate::mul_div::mult_div;


fn main() {
    let x = "9";
    //let mut eq1: String = String::from("$x - 555.5 - 777.7 + 5 + 6000 -8 $");

    
    let mut eq2 = String::from("$x * 2 * 3 / 7 * 3$");
    
    //let eq3 = String::from("$x * 3 + 2$");
    //let eq4 = String::from("$x * (3 + 2)$");
    //let eq2 = String::from("");
    //let eq2 = String::from("");
    let mut eqs: String = op::remove_whitespace(&mut eq2); // 9+5-7+5+6-8
    println!("eq inicial: {}", eq2);
    eqs = eqs.replace("x", &x);

    eqs = mult_div(eqs);
    
    soma_sub(eqs);
}
