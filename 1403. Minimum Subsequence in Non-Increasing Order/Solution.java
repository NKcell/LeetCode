import java.util;
import java.util.ArrayList;

class Solution {
    public List<Integer> minSubsequence(int[] nums) {
        Arrays.sort(nums);
        int sum = 0;
        for(int i=0; i<nums.length; i++){
            sum += nums[i];
        }

        int tmpSum = 0;
        int index = nums.length - 1;
        ArrayList<Integer> res = new ArrayList<>();

        while(index>=0){
            tmpSum += nums[index];
            sum -= nums[index];

            res.add(nums[index]);
            if(tmpSum>sum){
                return res;
            }
            index--;
        }

        return res;
    }
}