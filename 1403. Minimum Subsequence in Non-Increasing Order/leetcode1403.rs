impl Solution {
    pub fn min_subsequence(nums: Vec<i32>) -> Vec<i32> {
        let mut sum = 0;
        let mut tmp_sum = 0;
        let mut copy_nums = nums.clone();

        for i in &nums{
            sum += *i;
        }

        for i in 0..copy_nums.len()-1{
            for j in 0..copy_nums.len()-1-i{
                if copy_nums[j] > copy_nums[j+1]{
                    let tmp = copy_nums[j];
                    copy_nums[j] = copy_nums[j+1];
                    copy_nums[j+1] = tmp;
                }
            }
        }

        //println!("{:?}", copy_nums);

        let mut res: Vec<i32> = Vec::new();
        while tmp_sum <= sum{
            if let Some(tmp) = copy_nums.pop(){
                sum -= tmp;
                tmp_sum += tmp;
                res.push(tmp);
            }
            
        }
        
        res
    }
}