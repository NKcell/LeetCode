#include<stdio.h>

int dominantIndex(int* nums, int numsSize){
    int a,b,index;

    if (numsSize<2){
        return 0;
    }

    if (*nums<*(nums+1)){
        a = *nums;
        b = *(nums+1);
        index = 1;
    }else{
        b = *nums;
        a = *(nums+1);
        index = 0;
    }

    for (int i=2; i<numsSize; i++){
        if (*(nums+i)>b){
            int tmp = b;
            b = nums[i];
            a = tmp;
            index = i;
        }else if (*(nums+i)>a){
            a = nums[i];
        }
    }

    if (b >= 2*a){
        return index;
    }
    return -1;
}

int main(){
    int nums[4] = {3, 6, 1, 0};
    printf("%d", dominantIndex(nums, 4));
    return 0;
}