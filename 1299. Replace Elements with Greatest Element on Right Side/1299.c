/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* replaceElements(int* arr, int arrSize, int* returnSize){
    int* res = (int* )malloc(sizeof(int)*arrSize);
    int max = -1;
    *returnSize = arrSize;
    for (int i = arrSize-1; i>-1; i--){
        *(res+i) = max;
        if (*(arr+i)>max){
            max = *(arr+i);
        }
    }
    return res;
}