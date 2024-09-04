pub fn remove_whitespace(s: &str) -> String {
    s.chars().filter(|c| !c.is_whitespace()).collect()
}
pub fn operacao(ch: char, n1: f64, n2: f64) -> f64 {
    if ch == '+' {
        return n1 + n2;
    } else if ch == '-' {
        return n1 - n2;
    }
    return 0.0;
}
