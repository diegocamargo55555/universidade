fn main() {
    secante();
}

fn secante() -> i32 {
    let (mut x0, mut x1, precisao, mut k) = (1.5, 1.7, 0.003, 100);
    let mut x2 = 0.0;
    let mut raiz = 0.0; 

    let (mut funck, mut funckneg) = (0.0, 0.0);
        println!("fim:{}", modulo(funcao(x0)));

    if modulo(funcao(x0)) > precisao {
        if modulo(funcao(x1)) < precisao && modulo(x1 - x0) < precisao {
            raiz = x1;
        } else {
            let mut n = 0;
            while modulo(funcao(x1)) > precisao && k > n && modulo(x1 - x0) > precisao {
                n += 1;
                funck = funcao(x1);
                funckneg = funcao(x0);
                x2 = x1 - (funcao(x1) * (x1 - x0)) / (funcao(x1) - funcao(x0));
                x0 = x1;
                x1 = x2;
            }
            raiz = x2;
        }
    } else {
        raiz = x1;
    }
    println!("x0:{}", x0);
    println!("x1:{}", x1);
    println!("x2:{}", x2);
    println!("raiz:{}", raiz);

    return 0;

}

fn modulo(a: f64) -> f64 {
    if a >= 0.0 {
        return a;
    } else {
        return -a;
    }
}

fn funcao(x: f64) -> f64 {
    return x * x + x - 6.0;
}
