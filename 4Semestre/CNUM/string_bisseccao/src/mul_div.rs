use core::f64;

use crate::op::get_all;
use crate::op::operacao;
use crate::op::remove_whitespace;

pub fn posi_mult_div(eqs: String) -> Vec<usize> {
    let (mut mult2, mut div2, cifrao) = (98, 98, 0);
    let cifrao2: usize = eqs.len() - 1; // pega a ultima posição do vetor

    let mult = eqs.chars().position(|c| c == '*').unwrap_or(99);
    if mult != 99 {
        mult2 = eqs[mult + 1..].chars().position(|c| c == '*').unwrap_or(99) + mult + 1;
    }

    let div = eqs.chars().position(|c| c == '/').unwrap_or(99);
    if div != 99 {
        div2 = eqs[div + 1..].chars().position(|c| c == '*').unwrap_or(99) + div + 1;
    }

    let mut v: Vec<usize> = vec![cifrao, mult, mult2, div, div2, cifrao2];
    v.sort();

    return v;
}

pub fn mult_div(mut eqs: String) -> String {
    let mut repet = eqs.chars().filter(|c| *c == '*').count();
    repet += eqs.chars().filter(|c| *c == '/').count();

    for _i in 0..repet {
        println!("a");
        eqs = remove_whitespace(&mut eqs);
        println!("--------\ninicio: {}", eqs);

        let v = posi_mult_div(eqs.clone());
        println!("vetor{:?}", v);

        eqs = do_mult_div(eqs.clone(), &v);

        println!("fim: {}", eqs);
    }

    return eqs;
}

pub fn do_mult_div(mut eqs: String, v: &Vec<usize>) -> String {
    let (s1, s2, n2, resultado, sinal);
    let sinal_posi: usize;
    let n1: f64;
    let td_posicoes = get_all(eqs.clone());

    sinal = eqs.chars().nth(v[1]).unwrap();
    sinal_posi = eqs[2..].chars().position(|s| s == sinal).unwrap() + 2;
    let antes_sinal: usize = td_posicoes.iter().position(|n| n == &sinal_posi).unwrap() - 1;
    let next_sinal: usize = td_posicoes.iter().position(|n| n == &sinal_posi).unwrap() + 1;

    //pega os numeros que serão usados na operação

//55*3 +5 *2*5+6
//55*-3

    println!("td_posicoes:{:?} \nantes: {} \nsinal: {}",td_posicoes, antes_sinal, sinal_posi);
    println!("s1:{}", &eqs[td_posicoes[antes_sinal]+1..sinal_posi]);
    s1 = &eqs[td_posicoes[antes_sinal]+1..sinal_posi];
    n1 = s1.parse().unwrap();


    if &eqs[sinal_posi + 1..td_posicoes[next_sinal]]=="" {
        s2 = &eqs[sinal_posi + 1..td_posicoes[next_sinal+1]];
    }else {
        s2 = &eqs[sinal_posi + 1..td_posicoes[next_sinal]];
    }

    //55*-3
    println!("s2:{}", &eqs[sinal_posi + 1..td_posicoes[next_sinal]]);
    n2 = s2.parse().unwrap();

    resultado = operacao(sinal, n1, n2);
    let resultado_str = resultado.to_string();

    if &eqs[sinal_posi + 1..td_posicoes[next_sinal]]=="" {
        eqs.replace_range(
            td_posicoes[antes_sinal]+1..td_posicoes[next_sinal+1],
            &resultado_str,
        ); //
        }else {
        eqs.replace_range(
            td_posicoes[antes_sinal]+1..td_posicoes[next_sinal],
            &resultado_str,
        ); //
        }

    return eqs;
}
