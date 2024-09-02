


fn main() {
    //let a = 5.0;
    //let b = 8.0;

    let mut resultado = 0.0; 


    let mut eq1 = String::from("$9 + 5 - 7 + 5 + 6 -8 $");

    let s =remove_whitespace(&mut eq1); // 9+5-7+5+6-8




    //let eq2 = String::from("$x + 2 * 3$");
    //let eq3 = String::from("$x * 3 + 2$");
    //let eq4 = String::from("$x * (3 + 2)$");
    //let eq2 = String::from("");
    //let eq2 = String::from("");

    println!("{}", s);

    let menos: usize = s.chars().position(|c|c == '-').unwrap();
    let mais = s.chars().position(|c|c == '+').unwrap();
    let cifrao = s.chars().position(|c|c == '$').unwrap();

    let mut v = vec![cifrao, menos, mais];
    v.sort();

    let ch = s.chars().nth(v[1]).unwrap();

    let s1= &s[v[0]+1..v[1]];
    let n1: f64 =  s1.parse().unwrap();

    let s2 = &s[v[1]+1..v[2]];
    let n2: f64 =  s2.parse().unwrap();

    println!("n1:{} \nn2:{}", n1, n2);

    resultado = operacao(ch, n1, n2);


    println!("valor:{}", resultado);

    

}

fn remove_whitespace(s: &str) -> String {
    s.chars().filter(|c| !c.is_whitespace()).collect()
}
fn operacao(ch: char, n1: f64, n2: f64) -> f64{
    if ch == '+' {
        return n1 + n2;
    }
    else if ch == '-' {
        return n1 - n2;        
    }

    return 0.0;
    
}

/*
    for x in v {
        println!("{}", x)
    }

*/