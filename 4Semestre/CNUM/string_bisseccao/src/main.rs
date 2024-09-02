
fn main() {
    //let a = 5.0;
    //let b = 8.0;

    let mut resultado = 0.0; 


    let mut eq1: String = String::from("$9 - 5 - 7 - 5 + 6 -8 $");
    //let eq2 = String::from("$x + 2 * 3$");
    //let eq3 = String::from("$x * 3 + 2$");
    //let eq4 = String::from("$x * (3 + 2)$");
    //let eq2 = String::from("");
    //let eq2 = String::from("");
    let mut eqs: String =remove_whitespace(&mut eq1); // 9+5-7+5+6-8

    let mut menos: usize = 98;
    let mut menos2: usize = 98;
    let mut mais: usize = 98;
    let mut mais2: usize = 98;
    let mut cifrao: usize = 0;
    let mut cifrao2: usize = eqs.len() - 1;
    let mut s1 = "0";
    let mut n1 = 0.0;
    let mut s2 = "0";
    let mut n2 = 0.0;
    let mut ch ='c'; 


    for i in 0..6 {

        eqs = remove_whitespace(&mut eqs); // 9+5-7+5+6-8

        println!("--------\ninicio: {}", eqs);

        menos = eqs.chars().position(|c|c == '-').unwrap_or(99);
        if menos != 99 {
            menos2= eqs[menos+1..].chars().position(|c|c == '-').unwrap_or(99) + menos+1;
            //println!("menos2: {}", &eqs[menos+2..]);
        }

        mais = eqs.chars().position(|c|c == '+').unwrap_or(99);
        if mais != 99{
            mais2 = eqs[mais+1..].chars().position(|c|c == '+').unwrap_or(99) + mais+1;
            //println!("mais2: {}", &eqs[mais+2..]);
        }     
        cifrao2 = eqs.len() - 1; // pega a ultima posição do vetor

        let mut v: Vec<usize> = vec![cifrao, menos, mais, mais2, menos2, cifrao2];
        v.sort();
        println!("vetor{:?}", v);

        // $-3-7+5+6-8$
        if &eqs[1..2] == "-" {
            ch = eqs.chars().nth(v[2]).unwrap();
            s1 = &eqs[v[1]+1..v[2]];
            println!("s1: {}", &s1);
            n1 = s1.parse().unwrap();
            n1 = -n1;

            s2 = &eqs[v[2]+1..v[3]];
            println!("s2: {}", &s2);
            n2 =  s2.parse().unwrap();
        }else {
            ch = eqs.chars().nth(v[1]).unwrap(); // pega o simbolo da operação a ser executada

            //pega os numeros que serão usados na operação
            s1 = &eqs[v[0]+1..v[1]];
            println!("s1: {}", &s1);
            n1 = s1.parse().unwrap();

            println!("v1: {}", v[0]);
            println!("v2: {}", v[1]);

            s2 = &eqs[v[1]+1..v[2]];
            println!("s2: {}", &s2);
            n2 =  s2.parse().unwrap();
            //println!("n1:{} \nn2:{}", n1, n2);
        }

        resultado = operacao(ch, n1, n2);
        let mut resultadoSTR= resultado.to_string();

        eqs.replace_range(v[1]+1..v[1]+2, &resultadoSTR);
        eqs.replace_range(v[0]+1..v[1]+1, " ");

        println!("fim: {}", eqs);

        println!("valor:{}", resultado); 
        
    }
    println!("tes3: {}", eqs);


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

