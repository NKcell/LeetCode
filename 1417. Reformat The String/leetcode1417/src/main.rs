fn main() {
    println!("Hello, world!");
    let res = reformat("ab123".to_string());
    println!("{}", res);
}

fn reformat(s: String) -> String {
    let mut digit: Vec<String> = Vec::new();
    let mut letter: Vec<String> = Vec::new();
    let mut res = String::new();

    for i in s.chars(){
        if i>='0' && i<='9'{
            digit.push(i.to_string());
        }else{
            letter.push(i.to_string());
        }
    }

    let mut tmp = letter.len();
    if digit.len()>letter.len(){
        tmp = digit.len() - letter.len();
    }else{
        tmp = letter.len() - digit.len() ;
    }
    
    if tmp> 1{
        return String::new();
    }

    if digit.len()>letter.len(){
        for _ in 0..letter.len(){
            res += &digit.pop().unwrap();
            res += &letter.pop().unwrap();
        }
        res += &digit.pop().unwrap();
    }else if tmp == 0{
        for _ in 0..letter.len(){
            res += &digit.pop().unwrap();
            res += &letter.pop().unwrap();
        }
    }else{
        for _ in 0..digit.len(){
            res += &letter.pop().unwrap();
            res += &digit.pop().unwrap();
        }
        res += &letter.pop().unwrap();
    }
    res
}

fn reformat1(s: String) -> String {
    let n = s.len();
    let mut cache: Vec<char> = vec!['#'; n * 2 + 2];
    let (mut i, mut j) = (1_i32, 2_i32);
    for c in s.chars() {
        if c.is_numeric() {
            cache[i as usize] = c;
            i += 2;
        } else {
            cache[j as usize] = c;
            j += 2;
        }
    }
    // println!("{}{}", i, j);
    if i - j >= 3 || j - i > 3 {
        return "".to_string();
    }
    if (i - j).abs() > 1 {
        cache.swap(0, j as usize - 2);
    }
    cache.iter().filter(|c| **c != '#').collect::<String>()
}