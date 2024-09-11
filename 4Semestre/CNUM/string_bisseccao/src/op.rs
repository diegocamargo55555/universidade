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


pub fn do_sum_sub(mut eqs: String, v: &Vec<usize>) -> String
{
    let (s1, s2,n2, resultado, sinal,);
    let sinal_posi:usize;
    let n1: f64;
    let td_posicoes = get_all(eqs.clone());


    if &eqs[1..2] == "-"  {
        sinal = eqs.chars().nth(v[2]).unwrap();
        sinal_posi = eqs[2..].chars().position(|s| s == sinal).unwrap() + 2;
        let antes_sinal:usize = td_posicoes.iter().position(|n| n == &sinal_posi).unwrap() - 1;
        let next_sinal:usize = td_posicoes.iter().position(|n| n == &sinal_posi).unwrap() + 1;

        //pega os numeros que serão usados na operação
        s1 = &eqs[td_posicoes[antes_sinal] .. sinal_posi];
        n1 = s1.parse().unwrap();

        s2 = &eqs[sinal_posi + 1..td_posicoes[next_sinal]];
        n2 = s2.parse().unwrap();

        resultado = operacao(sinal, n1, n2);   

        let resultado_str = resultado.to_string();

        eqs.replace_range(td_posicoes[antes_sinal]..td_posicoes[next_sinal] , &resultado_str); //

        return eqs;
    }
    else 
    {
        sinal = eqs.chars().nth(v[1]).unwrap(); // pega o simbolo da operação a ser executada
        sinal_posi = eqs.chars().position(|s| s == sinal).unwrap();
        let antes_sinal:usize = td_posicoes.iter().position(|n| n == &sinal_posi).unwrap() - 1;
        let next_sinal:usize = td_posicoes.iter().position(|n| n == &sinal_posi).unwrap() + 1;

        //pega os numeros que serão usados na operação

        s1 = &eqs[td_posicoes[antes_sinal]+1 .. sinal_posi];
        n1 = s1.parse().unwrap();

        s2 = &eqs[sinal_posi + 1..td_posicoes[next_sinal]];
        n2 = s2.parse().unwrap();

        resultado = operacao(sinal, n1, n2);   
        let resultado_str = resultado.to_string();

        eqs.replace_range(td_posicoes[antes_sinal] + 1..td_posicoes[next_sinal] , &resultado_str); //

        return eqs;
    } 
}

pub fn get_all(eqs: String) -> Vec<usize> {
    let (mut mult2, mut div2, cifrao, mut menos2, mut mais2) = (98, 98, 0, 98, 98);
    let (mult,  div, menos, mais);
    let cifrao2: usize = eqs.len() - 1; // pega a ultima posição do vetor

    menos = eqs.chars().position(|c| c == '-').unwrap_or(99);
    if menos != 99 {
        menos2 = eqs[menos + 1..].chars().position(|c| c == '-').unwrap_or(99)+ menos + 1;
    }

    mais = eqs.chars().position(|c| c == '+').unwrap_or(99);
    if mais != 99 {
        mais2 = eqs[mais + 1..].chars().position(|c| c == '+').unwrap_or(99) + mais + 1;
    }

    mult = eqs.chars().position(|c| c == '*').unwrap_or(99);
    if mult != 99 {
        mult2 = eqs[mult + 1..].chars().position(|c| c == '*').unwrap_or(99)+ mult + 1;
    }

    div = eqs.chars().position(|c| c == '/').unwrap_or(99);
    if div != 99 {
        div2 = eqs[div + 1..].chars().position(|c| c == '*').unwrap_or(99)+ div + 1;
    }

    let mut v: Vec<usize> = vec![cifrao, mult, mult2,  div, div2, cifrao2, mais, menos, mais2, menos2];
    v.sort();

    return v;
}

    
