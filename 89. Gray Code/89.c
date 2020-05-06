
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* grayCode(int n, int* returnSize){
    int count = 1;
    for(int i=0; i<n; i++){
        count *= 2;
    }

    *returnSize = count;
    int* res = malloc(sizeof(int)*count);
    *(res+0) = 0;
    int tmpLen = 1;

    for(int j=0; j<n; j++){
        for(int x=0; x<tmpLen; x++){
            *(res+tmpLen+x) = *(res+tmpLen-x-1)+tmpLen;
        }
        tmpLen *= 2;
    }

    return res;
}