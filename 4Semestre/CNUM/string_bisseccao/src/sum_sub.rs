use crate::op::operacao;
use crate::op::remove_whitespace;

pub fn soma_sub(mut eqs: String) {
    let (mut menos, mut menos2, mut mais, mut mais2, cifrao) = (98, 98, 98, 98, 0);
    let (mut s1, mut s2, mut n1, mut n2, mut resultado, mut sinal) = ("0", "0", 0.0, 0.0, 0.0, 'c');
    let mut cifrao2: usize = eqs.len() - 1;
    let mut repet = eqs.chars().filter(|c| *c == '-').count();
    repet += eqs.chars().filter(|c| *c == '+').count();

    for i in 0..repet {
        eqs = remove_whitespace(&mut eqs); // 9+5-7+5+6-8

        println!("--------\ninicio: {}", eqs);

        menos = eqs.chars().position(|c| c == '-').unwrap_or(99);
        if menos != 99 {
            menos2 = eqs[menos + 1..]
                .chars()
                .position(|c| c == '-')
                .unwrap_or(99)
                + menos
                + 1;
            //println!("menos2: {}", &eqs[menos+2..]);
        }

        mais = eqs.chars().position(|c| c == '+').unwrap_or(99);
        if mais != 99 {
            mais2 = eqs[mais + 1..].chars().position(|c| c == '+').unwrap_or(99) + mais + 1;
            //println!("mais2: {}", &eqs[mais+2..]);
        }
        cifrao2 = eqs.len() - 1; // pega a ultima posição do vetor

        let mut v: Vec<usize> = vec![cifrao, menos, mais, mais2, menos2, cifrao2];
        v.sort();
        println!("vetor{:?}", v);

        // $-3-7+5+6-8$
        if &eqs[1..2] == "-" {
            sinal = eqs.chars().nth(v[2]).unwrap();

            s1 = &eqs[v[1] + 1..v[2]];
            n1 = s1.parse().unwrap();
            n1 = -n1;

            s2 = &eqs[v[2] + 1..v[3]];
            n2 = s2.parse().unwrap();

            println!("sinal: {}___n1:{},___n2:{}", sinal, n1, n2);
            resultado = operacao(sinal, n1, n2);
            let mut resultadoSTR = resultado.to_string();

            println!(
                "replace1: {}\nreplace2: {}",
                &eqs[v[1] + 1..v[1] + 2],
                &eqs[v[0] + 1..v[1] + 1]
            );
            eqs.replace_range(v[2] + 1..v[2] + 2, &resultadoSTR); //
            eqs.replace_range(v[1]..v[2] + 1, " "); //
        } else {
            sinal = eqs.chars().nth(v[1]).unwrap(); // pega o simbolo da operação a ser executada

            //pega os numeros que serão usados na operação
            s1 = &eqs[v[0] + 1..v[1]];
            n1 = s1.parse().unwrap();

            s2 = &eqs[v[1] + 1..v[2]];
            n2 = s2.parse().unwrap();

            println!("sinal: {}___n1:{},___n2:{}", sinal, n1, n2);
            resultado = operacao(sinal, n1, n2);
            let mut resultadoSTR = resultado.to_string();

            println!(
                "replace1: {}\nreplace2: {}",
                &eqs[v[1] + 1..v[1] + 2],
                &eqs[v[0] + 1..v[1] + 1]
            );
            eqs.replace_range(v[1] + 1..v[1] + 2, &resultadoSTR);
            eqs.replace_range(v[0] + 1..v[1] + 1, " ");
        }
        println!("fim: {}", eqs);

        println!("valor:{}", resultado);
    }
    println!("tes3: {}", eqs);
}
