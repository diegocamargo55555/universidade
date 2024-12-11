fn main() {
    newton();
}

fn newton() -> f64{
    let (mut x, precicao, max , mut k, mut x1) = (0.5, 0.01, 100, 0, 0.0);
    let mut fx =funcao(x);
    let mut f_linha;


    if modulo(fx) > precicao {
        k = 1;
        f_linha = funcao_linha(x);

        x1 = x - (fx/f_linha);
        fx =funcao(x1);

        while modulo(funcao(x1)) > precicao && modulo(x1 - x) > precicao && k <= max {
            k += 1;
            x = x1;
            f_linha = funcao_linha(x);
            x1 = x - (fx/f_linha);
            fx =funcao(x1);            
        }
        println!("fim x1: {}", x1);
        return x1;
    }else {
        println!("fim x: {}", x);
        return x;
    }
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

fn funcao_linha(x: f64) -> f64{
    return x.powf(3.0) *3.0 - 9.0;
}

