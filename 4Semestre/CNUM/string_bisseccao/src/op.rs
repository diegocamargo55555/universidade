use std::usize;

pub fn remove_whitespace(s: &str) -> String {
    s.chars().filter(|c| !c.is_whitespace()).collect()
}
pub fn operacao(ch: char, n1: f64, n2: f64) -> f64 {
    if ch == '+' {
        return n1 + n2;
    } 
    else if ch == '-' {
        return n1 - n2;
    } 
    else if ch == '*' {
        return n1 * n2;
    }
    else if ch == '/' {
        return  n1 / n2;
    }
    return 0.0;
}

pub fn posi_sum_sub(eqs: String) -> Vec<usize> { // pega a posição em que está o sinal e ordena em ordem crescente 
    let (mut menos2, mut mais2, cifrao) = (98, 98, 0);
    let (menos, mais);
    let cifrao2: usize = eqs.len() - 1; // pega a ultima posição do vetor

    menos = eqs.chars().position(|c| c == '-').unwrap_or(99);
    if menos != 99 {
        menos2 = eqs[menos + 1..].chars().position(|c| c == '-').unwrap_or(99)+ menos + 1;
    }

    mais = eqs.chars().position(|c| c == '+').unwrap_or(99);
    if mais != 99 {
        mais2 = eqs[mais + 1..].chars().position(|c| c == '+').unwrap_or(99) + mais + 1;
    }

    let mut v: Vec<usize> = vec![cifrao, menos, menos2, mais, mais2, cifrao2];
    v.sort();

    return v;
}
 
pub fn prep_troca(eqs: String, v: &Vec<usize>) -> String{

    let (s1, s2,n2, resultado, sinal);
    let mut n1: f64;

    if &eqs[1..2] == "-"  {
        sinal = eqs.chars().nth(v[2]).unwrap();
        
        s1 = &eqs[v[1] + 1..v[2]];
        n1 = s1.parse().unwrap();
        n1 = -n1;
        
        s2 = &eqs[v[2] + 1..v[3]];
        n2 = s2.parse().unwrap();
        
        resultado = operacao(sinal, n1, n2);
        println!("antes: {}", eqs);
        
        return resultado.to_string();
    }
    else 
    {
        sinal = eqs.chars().nth(v[1]).unwrap(); // pega o simbolo da operação a ser executada

        //pega os numeros que serão usados na operação
        s1 = &eqs[v[0] + 1..v[1]];
        n1 = s1.parse().unwrap();

        s2 = &eqs[v[1] + 1..v[2]];
        n2 = s2.parse().unwrap();

        resultado = operacao(sinal, n1, n2);   
        return resultado.to_string();
     
    }

    

    
    


}