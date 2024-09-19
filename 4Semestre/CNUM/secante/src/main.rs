fn main() {
    secante();


}

fn secante() -> i32 {
    let (mut x0, mut x1, mut precisao , mut k ) =(0.0, 1.0, 0.01, 100 );
    let mut x2 = 0.0;
    
    if modulo(funcao(x0)) < precisao{
        println!("fim:{}", x0);
        return 0 ;
    }
    else if modulo(funcao(x1)) < precisao || modulo(x1-x0) < precisao {
        println!("fim:{}", x1);
        return 0 ;
    }

    k = 1;

    for _ in 0..10 {

        //x2 = x1 - ((funcao(x1) * (x0 - x1)) / (funcao(x1) - funcao(x0)));
        x2 = x1 - (funcao(x1)*(x1-x0))/(funcao(x1) - funcao(x0));

        println!("x0:{}\n x1:{}\n x2:{}\n", x0, x1, x2);


        if modulo(funcao(x2)) < precisao || modulo(x2-x1) < precisao {
            println!("fim:{}", x2);
            return 0;
        }
        x0 = x1;
        x1 = x2;
        k += 1;
    }
    println!("k: {}", k);
    return 0;


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
    return x.powf(3.0) - 0.5;
}