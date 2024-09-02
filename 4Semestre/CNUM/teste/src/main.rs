fn main() {
    let eq1 = String::from("$9 + 5 - 7 + 5 + 6 -8 $");

    let menos: usize = eq1.chars().position(|c|c == '*').unwrap_or(999);

    let mut v = vec![0, menos, 5];
    v.sort();


    let s1= &eq1[v[0]+1..v[1]];

    println!("{}", s1)






    

}
