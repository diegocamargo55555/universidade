use rayon::prelude::*;
use std::time::Instant; // Importa o cronômetro

fn main() {
    // Inicia o cronômetro para o programa inteiro (incluindo setup)
    let tempo_total = Instant::now();

    let passos = 100_000;
    let h = 1.0 / passos as f64;

    // Inicia o cronômetro especificamente para o cálculo paralelo
    let tempo_calculo = Instant::now();

    let soma: f64 = (0..passos)
        .into_par_iter()
        .map(|i| {
            let x = (i as f64 + 0.5) * h;
            4.0 / (1.0 + x * x)
        })
        .sum();

    let duracao_calculo = tempo_calculo.elapsed(); // Para o cronômetro do cálculo
    let pi = soma * h;
    let duracao_total = tempo_total.elapsed(); // Para o cronômetro total

    println!("Valor calculado de Pi: {:.15}", pi);
    println!("Valor real de Pi:      {:.15}", std::f64::consts::PI);
    println!("Diferença:             {:.15}", (pi - std::f64::consts::PI).abs());
    
    println!("---");
    println!("Tempo apenas do cálculo: {:?}", duracao_calculo);
    println!("Tempo total de execução: {:?}", duracao_total);
}