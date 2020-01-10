/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sumZero(int n, int* returnSize){
    *returnSize = n;
    int* res = (int*)malloc(sizeof(int)*n);

    if (n%2 == 1){
        n--;
        *(res+n) = 0;
    }

    while(n != 0){
        *(res+n-1) = n;
        *(res+n-2) = -n;
        n -= 2;
    }

    return res;
}