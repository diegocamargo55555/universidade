pub fn expo(eqs: String) -> Vec<usize> {
    let (mut mult2, mut div2, cifrao) = (98, 98, 0);
    let cifrao2: usize = eqs.len() - 1; // pega a ultima posição do vetor

    let mult = eqs.chars().position(|c| c == '*').unwrap_or(99);
    if mult != 99 {
        mult2 = eqs[mult + 1..].chars().position(|c| c == '*').unwrap_or(99) + mult + 1;
    }

    let div = eqs.chars().position(|c| c == '/').unwrap_or(99);
    if div != 99 {
        div2 = eqs[div + 1..].chars().position(|c| c == '*').unwrap_or(99) + div + 1;
    }

    let mut v: Vec<usize> = vec![cifrao, mult, mult2, div, div2, cifrao2];
    v.sort();

    return v;
}