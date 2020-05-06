impl Solution {
    pub fn permute(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut res: Vec<Vec<i32>>  = Vec::new();
        let tmp: Vec<i32> = Vec::new(); 

        Solution::dfs(&mut res, nums, tmp);

        res
}

    pub fn dfs(res: &mut Vec<Vec<i32>>, nums:Vec<i32>, tmp: Vec<i32>){
        if nums.len() == 0{
            res.push(tmp);
            return;
        }

        for i in 0..nums.len(){
            let mut newtmp = tmp.clone();
            newtmp.push(nums[i]);
            let mut newnums = nums.clone();
            newnums.remove(i);
            Solution::dfs(res, newnums, newtmp);
        }
    }
}