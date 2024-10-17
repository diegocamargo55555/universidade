fn main() {
    mil();
}

fn mil() -> f64{
    let (mut x, precicao, max , mut k, mut x1) = (0.0, 0.0001, 100, 0, 0.0);
    let mut xant = 0.0;
    if modulo(funcao(x)) > precicao {
        x = funcao_iterativa(x);
        while modulo(funcao(x)) > precicao && modulo(x- xant) > precicao && k <= max{
            xant = x;
            x = funcao_iterativa(xant);
            k += 1;
        }
    }
    println!("fim: {}", x);
    return x; 

}


fn modulo(a: f64 ) -> f64{

    if a >= 0.0 {
        return a;
    }
    else {
        return -a;
    }
}

fn funcao(x: f64) -> f64{
    return x.powf(3.0) - 9.0*x +3.0;
}

fn funcao_iterativa(x: f64) -> f64{
    return -3.0/(x.powf(2.0) - 9.0);
}
