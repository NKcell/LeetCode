int minStartValue(int* nums, int numsSize){
    int res = 0;
    int tmp = 0;

    for(int i=0; i<numsSize; i++){
        tmp += *(nums+i);
        if(tmp<res){
            res = tmp;
        }
    }

    return (res-1)*-1;
}