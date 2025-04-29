use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
mod tratar_linha;
use crate::io::BufReader;
use tratar_linha::{total_x, preenchex};
use tratar_linha::tirarX;
fn main() {
    let total_x = total_x;
    if let Ok(lines) = read_lines(
        "/home/heilt/Documents/universidade/5Semestre/Pesquisa_OP/read_file/src/novo.txt",
    ) {
        let mut x = 1;
        for mut line in lines.map_while(Result::ok) {
            //line = tirarX(line.clone());

            println!("eq{}: \t {}", x, line);
            x = x + 1;
        }

        total_x();
        preenchex();
    }
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
