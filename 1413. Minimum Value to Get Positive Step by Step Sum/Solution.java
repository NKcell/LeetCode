class Solution {
    public int minStartValue(int[] nums) {
        int res = 0;
        int tmp = 0;

        for(int i=0; i<nums.length; i++){
            tmp += nums[i];
            if (tmp<res){
                res = tmp;
            }
        }

        return (res-1)*-1;
    }
}