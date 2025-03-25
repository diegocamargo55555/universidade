pub fn tirarX(line: String) -> String{
    let mut x: usize = line.find("x").unwrap();
    println!("{}", x);

    let mut single = &line[x..x+1];
    while single != " "{
        
        x = x+1;
        single = &line[x..x+1];
    }
    println!("{}", line);
    return line;
}