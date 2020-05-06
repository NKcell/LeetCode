fn main() {
    println!("Hello, world!");
    let v = vec![1,-2,-3];
    println!("{}", min_start_value(v));
}

fn min_start_value(nums: Vec<i32>) -> i32 {
    let mut res = 0;
    let mut tmp = 0;

    for i in nums{
        tmp += i;
        if tmp<res{
            res = tmp;
        }
    }

    (res-1)*-1
}