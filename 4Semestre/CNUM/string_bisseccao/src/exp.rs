use crate::op::get_all;
use crate::op::operacao;
use crate::op::remove_whitespace;

pub fn exp_posi(eqs: String) -> Vec<usize> {
    let (mut exp2, cifrao) = (98, 0);
    let cifrao2: usize = eqs.len() - 1; // pega a ultima posição do vetor

    let exp= eqs.chars().position(|c| c == '^').unwrap_or(99);
    if exp != 99 {
        exp2 = eqs[exp + 1..].chars().position(|c| c == '^').unwrap_or(99) + exp + 1;
    }

    let mut v: Vec<usize> = vec![cifrao, exp, exp2, cifrao2];
    v.sort();

    return v;
}

pub fn exp_main(mut eqs: String) -> String {
    let repet = eqs.chars().filter(|c| *c == '^').count();

    for _i in 0..repet {
        println!("a");
        eqs = remove_whitespace(&mut eqs);
        println!("--------\ninicio: {}", eqs);

        let v = exp_posi(eqs.clone());
        println!("vetor{:?}", v);

        eqs = do_exp(eqs.clone(), &v);

        println!("fim: {}", eqs);
    }

    return eqs;
}

pub fn do_exp(mut eqs: String, v: &Vec<usize>) -> String {
    let (s1, s2, n2, resultado, sinal, sinal_posi, n1);
    let td_posicoes = get_all(eqs.clone());

    sinal = eqs.chars().nth(v[1]).unwrap(); // pega posição do sinal
    sinal_posi = eqs[2..].chars().position(|s| s == sinal).unwrap() + 2;
    let antes_sinal: usize = td_posicoes.iter().position(|n| n == &sinal_posi).unwrap() - 1;
    let next_sinal: usize = td_posicoes.iter().position(|n| n == &sinal_posi).unwrap() + 1;

    //pega os numeros que serão usados na operação
    s1 = &eqs[td_posicoes[antes_sinal]+1..sinal_posi];
    n1 = s1.parse().unwrap();


    if &eqs[sinal_posi + 1..td_posicoes[next_sinal]]=="" {
        s2 = &eqs[sinal_posi + 1..td_posicoes[next_sinal+1]];
    }else {
        s2 = &eqs[sinal_posi + 1..td_posicoes[next_sinal]];
    }

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