mod op;
mod sum_sub;
use crate::sum_sub::soma_sub;

fn main() {
    let x = "9";
    let mut eq1: String = String::from("$x + 5 - 7 + 5 + 6 -8 $");

    //let eq2 = String::from("$x + 2 * 3$");
    //let eq3 = String::from("$x * 3 + 2$");
    //let eq4 = String::from("$x * (3 + 2)$");
    //let eq2 = String::from("");
    //let eq2 = String::from("");
    let mut eqs: String = op::remove_whitespace(&mut eq1); // 9+5-7+5+6-8
    println!("eq inicial: {}", eq1);
    eqs = eqs.replace("x", &x);

    soma_sub(eqs);
}
