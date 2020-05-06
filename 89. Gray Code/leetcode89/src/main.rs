fn main() {
    println!("Hello, world!");
    let res = gray_code(2);
    println!("{:?}", res);
}


fn gray_code(n: i32) -> Vec<i32> {
    let mut res:Vec<i32> = Vec::new();

    res.push(0);

    for _ in 0..n{
        let tmp = res.len();
        for i in 0..tmp{
            res.push(res[tmp-i-1] + tmp as i32);
        }
    }

    res
}