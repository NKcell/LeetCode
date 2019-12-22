int abs(int x){
    if (x<0){
        return -x;
    }
    return x;
}

int* findDuplicates(int* nums, int numsSize, int* returnSize){
    int* res = (int*)malloc(sizeof(int)*numsSize);
    *returnSize = 0;
    for (int i=0; i<numsSize; i++){
        if (nums[abs(nums[i])-1]<0){
            *(res + *returnSize) = abs(nums[i]);
            (*returnSize) ++;
        }else{
            nums[abs(nums[i])-1] *= -1;
        }
    }
    return res;
}