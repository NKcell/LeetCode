fn main() {
    println!("Hello, world!");
    let res = combine(4, 2);
    println!("{:?}", res);
}

fn combine(n: i32, k: i32) -> Vec<Vec<i32>> {
        let mut res: Vec<Vec<i32>> = Vec::new();
        let mut nums: Vec<i32> = Vec::new();
        for i in 1..n+1{
            nums.push(i as i32);
        }

        dfs(&mut res, vec![], nums, k as usize);
        res
}

fn dfs(res: &mut Vec<Vec<i32>>, tmp: Vec<i32>,mut nums: Vec<i32>, n: usize){
    if n == 0{
        res.push(tmp);
        return;
    }

    if nums.len() < n{
        return;
    }

    let mylen = nums.len();
    for i in 0..mylen{
        if mylen - i < n{
            break;
        }

        let mut newtmp = tmp.clone();
        newtmp.push(nums[0]);
        nums.remove(0);
        let newnums = nums.clone();
        dfs(res, newtmp, newnums, n-1);
    }
}