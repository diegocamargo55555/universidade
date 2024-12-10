use crate::op::remove_whitespace;
use crate::op::get_all;

pub fn sin(mut eqs: String) -> String {
    eqs = eqs.replace("sin+", "sin");
    eqs = eqs.replace("sin-", "-sin");
    let repet = eqs.matches("sin").count();
    for _i in 0..repet {
        eqs = remove_whitespace(&mut eqs);
        println!("--------\ninicio: {}", eqs);

        let sin_posi = eqs.find("sin").unwrap() + 3;
        let temp_str = &eqs[sin_posi..];
        let td_posicoes = get_all(temp_str.to_string());

        println!("test2: {}", &eqs[sin_posi..td_posicoes[1]+sin_posi]);

        let mut result: f64 = eqs[sin_posi..td_posicoes[1]+sin_posi].parse().unwrap();
        result = result.sin();

        println!("result: {}", result);
        eqs.replace_range(sin_posi-3..td_posicoes[1]+sin_posi, &result.to_string()); //
        

        println!("fim: {}", eqs);
    }
    eqs = eqs.replace("--", "+");


    return eqs;
}

pub fn cos(mut eqs: String) -> String {
    eqs = eqs.replace("cos+", "cos");
    eqs = eqs.replace("cos-", "cos");
    let repet = eqs.matches("cos").count();
    for _i in 0..repet {
        eqs = remove_whitespace(&mut eqs);
        println!("--------\ninicio: {}", eqs);

        let cos_posi = eqs.find("cos").unwrap() + 3;
        let temp_str = &eqs[cos_posi..];
        let td_posicoes = get_all(temp_str.to_string());

        println!("test2: {}", &eqs[cos_posi..td_posicoes[1]+cos_posi]);

        let mut result: f64 = eqs[cos_posi..td_posicoes[1]+cos_posi].parse().unwrap();
        result = result.cos();

        println!("result: {}", result);
        eqs.replace_range(cos_posi-3..td_posicoes[1]+cos_posi, &result.to_string()); //

        println!("fim: {}", eqs);
    }

    return eqs;
}

pub fn tan(mut eqs: String) -> String {
    eqs = eqs.replace("tan+", "tan");
    eqs = eqs.replace("tan-", "-tan");
    let repet = eqs.matches("tan").count();
    for _i in 0..repet {
        eqs = remove_whitespace(&mut eqs);
        println!("--------\ninicio: {}", eqs);

        let tan_posi = eqs.find("tan").unwrap() + 3;
        let temp_str = &eqs[tan_posi..];
        let td_posicoes = get_all(temp_str.to_string());

        println!("test2: {}", &eqs[tan_posi..td_posicoes[1]+tan_posi]);

        let mut result: f64 = eqs[tan_posi..td_posicoes[1]+tan_posi].parse().unwrap();
        result = result.tan();

        println!("result: {}", result);
        eqs.replace_range(tan_posi-3..td_posicoes[1]+tan_posi, &result.to_string()); //

        println!("fim: {}", eqs);
    }
    eqs = eqs.replace("--", "+");


    return eqs;
}


pub fn cotan(mut eqs: String) -> String {
    eqs = eqs.replace("cotan+", "cotan");
    eqs = eqs.replace("cotan-", "-cotan");
    let repet = eqs.matches("cotan").count();
    for _i in 0..repet {
        eqs = remove_whitespace(&mut eqs);
        println!("--------\ninicio: {}", eqs);

        let cotan_posi = eqs.find("cotan").unwrap() + 3;
        let temp_str = &eqs[cotan_posi..];
        let td_posicoes = get_all(temp_str.to_string());

        println!("test2: {}", &eqs[cotan_posi..td_posicoes[1]+cotan_posi]);

        let mut result: f64 = eqs[cotan_posi..td_posicoes[1]+cotan_posi].parse().unwrap();
        result = 1.0/result.tan();

        println!("result: {}", result);
        eqs.replace_range(cotan_posi-3..td_posicoes[1]+cotan_posi, &result.to_string()); //
        

        println!("fim: {}", eqs);
    }
    eqs = eqs.replace("--", "+");


    return eqs;
}


pub fn cossec(mut eqs: String) -> String {
    eqs = eqs.replace("cossec+", "cossec");
    eqs = eqs.replace("cossec-", "-cossec");
    let repet = eqs.matches("cossec").count();
    for _i in 0..repet {
        eqs = remove_whitespace(&mut eqs);
        println!("--------\ninicio: {}", eqs);

        let cossec_posi = eqs.find("cossec").unwrap() + 3;
        let temp_str = &eqs[cossec_posi..];
        let td_posicoes = get_all(temp_str.to_string());

        println!("test2: {}", &eqs[cossec_posi..td_posicoes[1]+cossec_posi]);

        let mut result: f64 = eqs[cossec_posi..td_posicoes[1]+cossec_posi].parse().unwrap();
        result = 1.0/result.sin();

        println!("result: {}", result);
        eqs.replace_range(cossec_posi-3..td_posicoes[1]+cossec_posi, &result.to_string()); //
        

        println!("fim: {}", eqs);
    }
    eqs = eqs.replace("--", "+");


    return eqs;
}

pub fn sec(mut eqs: String) -> String {
    eqs = eqs.replace("sec+", "sec");
    eqs = eqs.replace("sec-", "sec");
    let repet = eqs.matches("sec").count();
    for _i in 0..repet {
        eqs = remove_whitespace(&mut eqs);
        println!("--------\ninicio: {}", eqs);

        let sec_posi = eqs.find("sec").unwrap() + 3;
        let temp_str = &eqs[sec_posi..];
        let td_posicoes = get_all(temp_str.to_string());

        println!("test2: {}", &eqs[sec_posi..td_posicoes[1]+sec_posi]);

        let mut result: f64 = eqs[sec_posi..td_posicoes[1]+sec_posi].parse().unwrap();
        result = 1.0/result.cos();

        println!("result: {}", result);
        eqs.replace_range(sec_posi-3..td_posicoes[1]+sec_posi, &result.to_string()); //

        println!("fim: {}", eqs);
    }
    return eqs;
}
