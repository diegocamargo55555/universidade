mod mul_div;
mod op;
mod sum_sub;
use op::do_eq;
use crate::mul_div::mult_div;
use crate::sum_sub::soma_sub;
mod exp;
use crate::exp::exp_main;
mod trigonometrico;

//use crate::exp::expo;

fn main() {
    let x = "-2";
    //let mut eq2: String = String::from("$55*-3 $");
    //let mut eq2 = String::from("$x * 2 * 3 / 77 - 3* 99 *5 +23 +5$");
    //let mut eq2 = String::from("$78 +54 -99 - 55 -45 +15 $");
    //let mut eq2 = String::from("$-78 ++54 -99 - 55 -45 +15 $");
    //let mut eq2 = String::from("$-(9^2) +2/(3+5)$");
    //let mut eq2 = String::from("$x * (3 + 2)$");

    let mut eq2 = String::from("$ sin -52*-6 +sin6$");
    //let mut eq2 = String::from("$ 5-(10-32)$");




    let mut eqs: String = op::remove_whitespace(&mut eq2); // 9+5-7+5+6-8
    println!("eq inicial: {}", eq2);
    eqs = eqs.replace("x", &x);
    eqs = eqs.replace("e", "2.7182818284590451");


    let repet = eqs.chars().filter(|c| *c == '(').count();

    for i in 0..repet+1 {
        let p_fim = eqs.chars().position(|c| c == ')').unwrap_or(99);

        if p_fim == 99 {
            let result = do_eq(eqs.to_string());
            println!("fim: {}", result);
            println!("if: {}", i);

        } else {
            let str_temp = &eqs[0..p_fim - 1];
            let p_ini = str_temp.rfind('(').unwrap_or(99);

            println!("first(): {}", &eqs[p_ini + 1..p_fim]);

            let mut temp_eq = eqs[p_ini + 1..p_fim].to_string();
            temp_eq.insert(p_fim - p_ini - 1, '$'); // (45)
            temp_eq.insert(0, '$');

            let result = do_eq(temp_eq).replace('$', "");
            eqs.replace_range(p_ini..p_fim + 1, &result);

            println!("fim: {}", eqs);
            println!("i: {}", i);

        }
    }

    /*     eqs = exp_main(eqs);
       println!("\nEXP: {}", eqs);

       eqs = mult_div(eqs);

       println!("\nsoma: {}", eqs);
       soma_sub(eqs);
    */
}
