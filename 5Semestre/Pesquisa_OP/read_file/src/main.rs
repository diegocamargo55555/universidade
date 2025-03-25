use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
mod tratar_linha;
use tratar_linha::tirarX;

fn main() {
    // File hosts.txt must exist in the current path
    if let  Ok(lines) = read_lines("/home/heilt/Documents/universidade/5Semestre/Pesquisa_OP/read_file/src/novo.txt") {
        // Consumes the iterator, returns an (Optional) String
        let mut x = 1;
        for mut line in lines.map_while(Result::ok) {
            line = tirarX(line.clone());
            println!("eq:{} {}",x, line);
            x = x+1;
        }
    }
}

// The output is wrapped in a Result to allow matching on errors.
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
