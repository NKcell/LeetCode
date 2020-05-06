fn main() {
    println!("Hello, world!");
    let nums = vec![1,1,2];
    let res = permute_unique(nums);
    println!("{:?}",res);
}

fn permute_unique(nums: Vec<i32>) -> Vec<Vec<i32>> {
    let mut mynums = nums.clone();
    mynums.sort();
    let mut res = Vec::new();
    let tmp = Vec::new();
    dfs(&mut res, mynums, tmp);
    res
}

fn dfs(res: &mut Vec<Vec<i32>>, nums: Vec<i32>, tmp: Vec<i32>){
    if nums.len() == 0{
        res.push(tmp);
        return;
    }

    let mut pre = 0;
    for i in 0..nums.len(){
        let mut newtmp = tmp.clone();
        let mut newnum = nums.clone();
        if i == 0{
            pre = nums[0];
            newtmp.push(pre);
            newnum.remove(i);
            dfs(res, newnum, newtmp);
        }else{
            if nums[i] == pre{
                continue;
            }else{
                pre = nums[i];
                newtmp.push(pre);
                newnum.remove(i);
                dfs(res, newnum, newtmp);
            }
        }
    }
}

