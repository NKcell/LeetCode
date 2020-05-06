fn main() {
    println!("Hello, world!");
    let s = get_permutation(4, 9);
    println!("{}", s);
}

fn get_permutation(n: i32, k: i32) -> String {
    let mut res = String::from("");
    let mut n1 = n;
    let mut k1 = k;
    k1 -= 1;
    let mut tmp: Vec<String> = Vec::new();
    for i in 1..n+1{
        tmp.push(i.to_string());
    }

    while n1>0{
        n1 -= 1;
        let chushu = jie(n1);
        let index = k1/chushu;
        k1 = k1%chushu;
        res += &tmp[index as usize];
        tmp.remove(index as usize);
    }

    res
}

fn jie(mut n: i32) -> i32{
    let mut res = 1;
    while n>0{
        res *= n;
        n -= 1;
    }
    res
}
