fn main() {
    mil();
}

fn mil() -> f64{
    let (mut x, precicao, max , mut k) = (1.0, 0.001, 100, 0);
    let mut xant = x;

    if modulo(funcao(x)) > precicao {
        x = funcao_iterativa(xant);
        while modulo(funcao(x)) > precicao && modulo(funcao_iterativa(x)- funcao_iterativa(xant)) > precicao && k <= max{
            xant = x;
            x = funcao_iterativa(xant);
            k += 1;
        }
    }
    println!("x: {}", x);
    println!("X_ant: {}", xant);
    println!("raiz: {}", funcao_iterativa(x));


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
    return x*x*x - x -1.0;
}

fn funcao_iterativa(x: f64) -> f64{
    return 1.0/(x) + 1.0/(x*x);
}
