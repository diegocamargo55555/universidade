fn main() {
    println!("Hello, world!");
}

pub struct LinkedList<T> {
    pub val: Option<T>,
    pub next: Option<Box<LinkedList<T>>>,
}

impl LinkedList<i32> {
    fn new(val: i32) -> LinkedList<i32> {
        LinkedList { val: Some(val), next: None }
    }
}
