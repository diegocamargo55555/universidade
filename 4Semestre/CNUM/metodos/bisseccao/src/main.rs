use core::f64;

fn main() {
    let precisao = 0.1;
    let n = 100.0;
    
    let mut a = 2.0;
    let mut b = 3.0;
    let mut k = 0.0;
    let mut meio = 0.0;

    if modulo(a, b) > precisao {
        while modulo(a, b) > precisao && k< n {
            k += 1.0;
            meio = (a+b)/2.0 ;
            if funcao(a) * funcao(meio) < 0.0 {
                b = meio
            }
            else {
                a = meio
            }
        }
    }
    println!("Valor de a:{} \nValor de b:{} \nValor da raiz:{} \nNumero de interações:{}",a , b, meio, k );
}

fn modulo(a: f64, b: f64 ) -> f64{
    let media = a-b;

    if media >= 0.0 {
        return media;
    }
    else {
        return -media;
    }
}

fn funcao(x: f64) -> f64{
    return x.powf(3.0) - 10.0;
}