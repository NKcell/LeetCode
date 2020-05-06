

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* minSubsequence(int* nums, int numsSize, int* returnSize){
    for(int i=0; i<numsSize-1; i++){
        for(int j=0; j<numsSize-1-i; j++){
            if(*(nums+j) < *(nums+j+1)){
                int tmp = *(nums+j);
                *(nums+j) = *(nums+j+1);
                *(nums+j+1) = tmp;
            }
        }
    }

    int sum = 0;
    for(int k=0; k<numsSize; k++){
        sum += *(nums+k);
    }

    int index = 0;
    int tmpSum = 0;
    *returnSize = 0;
    int* res = (int*)malloc(sizeof(int)*(*returnSize));
    while (tmpSum<=sum){
        tmpSum += nums[index];
        sum -= nums[index];
        
        (*returnSize) ++;
        int* tmp = (int*)malloc(sizeof(int)*(*returnSize)); 
        memcpy(tmp, res, sizeof(int)*(*returnSize-1));
        *(tmp+(*returnSize)-1) = nums[index];
        free(res);
        res = tmp;
        index ++;
    }

    return res;
}