impl Solution {
    pub fn my_sum(tmp: & Vec<i32>) -> i32{
        let mut res = 0;

        for i in 0..tmp.len(){
            res += tmp.get(i).unwrap();
        }

        res
    }

    pub fn can_complete_circuit(gas: Vec<i32>, cost: Vec<i32>) -> i32 {
        if Solution::my_sum(&gas) < Solution::my_sum(&cost){
            return -1;
        }

        let mut start = 0;
        let mut remain = 0;

        for i in 0..gas.len(){
            remain = remain + gas.get(i).unwrap() - cost.get(i).unwrap();
            if remain < 0{
                start = i+1;
                remain = 0;
            }
        }

        start as i32
    }
}