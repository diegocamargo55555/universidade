fn main() {
    let x = "9";
    let mut eq1: String = String::from("$x - 5 - 7 + 5 + 6 -8 $");


    //let eq2 = String::from("$x + 2 * 3$");
    //let eq3 = String::from("$x * 3 + 2$");
    //let eq4 = String::from("$x * (3 + 2)$");
    //let eq2 = String::from("");
    //let eq2 = String::from("");
    let mut eqs: String =remove_whitespace(&mut eq1); // 9+5-7+5+6-8
    eqs = eqs.replace("x", &x);






    

}
