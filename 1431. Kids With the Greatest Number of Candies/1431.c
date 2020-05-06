/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* kidsWithCandies(int* candies, int candiesSize, int extraCandies, int* returnSize){
    *returnSize = candiesSize;
    bool* res = (bool*)malloc(candiesSize*sizeof(bool));
    memset(res, 0, candiesSize*sizeof(bool));
    int maxNum = getMax(candies,  candiesSize);
    for(int i=0; i<candiesSize; i++){
        if(*(candies+i)+extraCandies >= maxNum){
            *(res+i) = true;
        }else{
            *(res+i) = false;
        }
    }
    return res;
}

int getMax(int* candies, int candiesSize){
    int res = *(candies);
    for(int i=1; i<candiesSize; i++){
        if(*(candies+i) > res){
            res = *(candies+i);
        }
    }
    return res;
}