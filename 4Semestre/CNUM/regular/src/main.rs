fn main() {
    regular();
}

fn regular() -> i32{
    let (mut a , mut b, mut k , mut media ) = (0.0, 1.0, 100, 0.0);
    let (mut precisao1, mut precisao2) = (0.0005, 0.0005);
    let mut x = 0.0;
    let max = 100;
    let (mut t1, mut t2) = (0.0, 0.0);

    if modulo(b-a) < precisao1 {
        println!("1esta entre: {}  ,  {}", a, b);
        return 0 ;
    }
    if modulo(funcao(a)) < precisao2 || modulo(funcao(b)) < precisao2{
        println!("2escolha entre: {}  ,  {}", a, b);
        return 0 ;
    }
    k = 1;

    for kk in 0..max {
        println!("k:{}", kk);
        media = funcao(a);

        t1 = a*funcao(b) - b*funcao(a);
        t2 = funcao(b) - funcao(a);
        x = t1 / t2  ;
        println!("{}",x);




        if modulo(funcao(a)) < precisao2 || k > 100 {
            println!("3x: {}", x);
            return 0;
        }

        if media* funcao(x) > 0.0 {
            a = x;
        }else {
            b = x;
        }


        if modulo(b-a) < precisao1 {
            println!("4esta entre: {}  ,  {}", a, b);
            return 0 ;

        }
    }
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
    return x.powf(3.0) - 9.0*x +3.0;
}