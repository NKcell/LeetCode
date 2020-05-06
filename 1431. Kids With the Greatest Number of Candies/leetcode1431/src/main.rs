fn main() {
    println!("Hello, world!");
    println!("{:?}", kids_with_candies(vec![2,3,5,1,3], 3));
}

fn kids_with_candies(candies: Vec<i32>, extra_candies: i32) -> Vec<bool> {
    let mut res: Vec<bool> = Vec::new();
    let max_num = get_max(&candies);

    for i in 0..candies.len(){
        if candies[i]+extra_candies >= max_num{
            res.push(true);
        }else{
            res.push(false);
        }
    }

    res
}

fn get_max(candies: &Vec<i32>) -> i32{
    let mut res = candies[0];
    for i in 0..candies.len(){
        if candies[i]>res{
            res = candies[i];
        }
    }
    res
}