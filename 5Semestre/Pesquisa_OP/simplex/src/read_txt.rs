


use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
extern crate matrix;

use matrix::prelude::*;


pub fn printline() {
    //let total_x = contar_x;

    if let Ok(lines) = read_lines("texto.txt") {
        let mut x = 1;
        for line in lines.map_while(Result::ok) {
            println!("eq{}: \t {}", x, line);
            x = x + 1;
        }
    } else {
        println!("not found")
    }

    //[macro_use]

    let mut sparse = Compressed::zero((2, 4));
    sparse.set((0, 0), 42.0);
    sparse.set((1, 3), 69.0);

    let dense = Conventional::from(&sparse);
    assert!(
        &*dense
            == &*matrix![
                42.0, 0.0, 0.0,  0.0;
                 0.0, 0.0, 0.0, 69.0;
            ]
    );
}
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
