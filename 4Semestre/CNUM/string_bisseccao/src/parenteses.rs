use crate::op::do_eq;


// 564(45+68(5/9*96*(45+59)))
pub fn parenteses(mut eqs: String){
    let pIni = eqs.rfind('(').unwrap_or(99);
    let pFim =eqs.chars().position(|c| c == ')').unwrap_or(99);    

    let result  = do_eq(eqs[pIni+1..pFim].to_string());


//    parenteses(eqs[pIni+1..pFim].to_string());   
    
}
