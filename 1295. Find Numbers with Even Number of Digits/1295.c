int findNumbers(int* nums, int numsSize){
    int count = 0;
    for(int i=0; i<numsSize; i++){
        if (nums[i]!=0){
            int tmp = 0;
            while(nums[i]!=0){
                nums[i] = nums[i]/10;
                tmp++;
            }
            if (tmp%2 == 0){
                count ++;
            }
        }
    }
    return count;
}