use std::collections::HashMap;

fn main() {
    println!("{}", &(letter_combinations("23".to_string()))[0]);
}

fn letter_combinations(digits: String) -> Vec<String> {
    if digits.len() == 0{
        let x = vec![];
        return x;
    }

    let mut my_map: HashMap<char, String> = HashMap::new();
    my_map.insert('2', String::from("abc"));
    my_map.insert('3', String::from("def"));
    my_map.insert('4', String::from("ghi"));
    my_map.insert('5', String::from("jkl"));
    my_map.insert('6', String::from("mno"));
    my_map.insert('7', String::from("pqrs"));
    my_map.insert('8', String::from("tuv"));
    my_map.insert('9', String::from("wxyz"));

    let mut res = vec![String::from("")];

    for char_digits in digits.chars(){

        let mut newres: Vec<String> = Vec::new();
        for i in &res{
            if let Some(j) = my_map.get(&char_digits){
                for k in j.chars(){
                    let mut l  = i.clone();
                    l.push(k);
                    newres.push(l);
                }
            }
        }
        res = newres;
    }

    res
}
