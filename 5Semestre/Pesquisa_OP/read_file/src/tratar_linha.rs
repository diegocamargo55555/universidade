use std::fs::File;
use std::io::BufRead;
use crate::io::BufReader;
use crate::read_lines;

pub fn tirarX(mut line: String) -> String {

    while line.contains("x") {
        let mut x: usize = line.find("x").unwrap();

        while line[x..x + 1] != *" " {
            line.replace_range(x..x + 1, "1");

            line.replace_range(x + 1..x + 2, " ");

            x = x + 1;
        }
    }
    return line;
}

fn contX(line: String) -> usize {
    if line.contains("max") {
        return line.chars().filter(|c| *c == 'x').count() - 1;
    }
    return line.chars().filter(|c| *c == 'x').count();
}

pub fn total_x() -> usize {
    if let Ok(lines) = read_lines("/home/heilt/Documents/universidade/5Semestre/Pesquisa_OP/read_file/src/novo.txt",) {
        // Consumes the iterator, returns an (Optional) String
        let mut totalx = 0;
        for line in lines.map_while(Result::ok) {
            let temp = contX(line.clone());
            if totalx < temp {
                totalx = temp;
            }
        }
        println!("total de X:{}", totalx);
        return totalx;
    }
    return 0;
    
}


pub fn preenchex(){
    let f = File::open("/home/heilt/Documents/universidade/5Semestre/Pesquisa_OP/read_file/src/novo.txt").unwrap();
    let mut reader = BufReader::new(f);
    let mut number_of_lines: String = String::new().to_owned();
    reader.read_line(&mut number_of_lines);


    let first_line = 2;
    let totalx = total_x();
    println!("a: {}", number_of_lines);
    if number_of_lines.contains("max") || number_of_lines.contains("min") {

        for i in first_line+1..totalx+1 {
            let string_test = "+ x";

            number_of_lines.push_str(string_test).to_owned();
            
            number_of_lines.push_str(&i.to_string());


            
        }

    }
    println!("a: {}", number_of_lines);




}