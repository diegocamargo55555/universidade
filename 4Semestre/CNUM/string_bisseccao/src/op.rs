pub fn remove_whitespace(s: &str) -> String {
    s.chars().filter(|c| !c.is_whitespace()).collect()
}
pub fn operacao(ch: char, n1: f64, n2: f64) -> f64 {
    if ch == '+' {
        return n1 + n2;
    } else if ch == '-' {
        return n1 - n2;
    } else if ch == '*' {
    }
    return 0.0;
}

pub fn posi_sum_sub(eqs: String) -> Vec<usize> {
    let (mut menos2, mut mais2, cifrao) = (98, 98, 0);
    let (menos, mais);
    let cifrao2: usize = eqs.len() - 1; // pega a ultima posição do vetor

    menos = eqs.chars().position(|c| c == '-').unwrap_or(99);
    if menos != 99 {
        menos2 = eqs[menos + 1..]
            .chars()
            .position(|c| c == '-')
            .unwrap_or(99)
            + menos
            + 1;
    }

    mais = eqs.chars().position(|c| c == '+').unwrap_or(99);
    if mais != 99 {
        mais2 = eqs[mais + 1..].chars().position(|c| c == '+').unwrap_or(99) + mais + 1;
    }

    let mut v: Vec<usize> = vec![cifrao, menos, menos2, mais, mais2, cifrao2];
    v.sort();

    return v;
}
