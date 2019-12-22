#include <stdio.h>
#include <stdlib.h>
#include <cstdlib>

// leetcode运行会报错...

char isexist(int x, int y, int** queens, int queensSize){
    int* tmp= (int*) queens;
    for (int i=0; i<queensSize; i++){
        if ((*(tmp+i*2)) == x && (*(tmp+1+i*2)) == y){
            return 1;
        }
    }
    return 0;
}

int** queensAttacktheKing(int** queens, int queensSize, int* queensColSize, int* king, int kingSize, int* returnSize, int** returnColumnSizes){
    int x = *king;
    int y = *(king+1);

    int *res = (int *)malloc(sizeof(int)*8*2);
    int count = 0; 
    
    for (int i=-1; i<2; i++){
        for (int j=-1; j<2; j++){
            for (int k=1; k<8; k++){
                if (isexist(x+i*k, y+j*k, queens, queensSize)==1){
                    *(res+count) = x+i*k;
                    count++;
                    *(res+count) = y+j*k;
                    count++;
                    break;
                }
            }
        }
    }
    *returnSize = count/2;
    printf("%d\n", *returnSize);
    **returnColumnSizes = 2;
    return (int**)res;
}

int main(){
    int queens[][2] = {{5,6},{7,7},{2,1},{0,7},{1,6},{5,1},{3,7},{0,3},{4,0},{1,2},{6,3},{5,0},{0,4},{2,2},{1,1},{6,4},{5,4},{0,0},{2,6},{4,5},{5,2},{1,4},{7,5},{2,3},{0,5},{4,2},{1,0},{2,7},{0,1},{4,6},{6,1},{0,6},{4,3},{1,7}};
    int queensSize = 34;
    int *queensColSize;
	int tmp = 20;
    queensColSize = &tmp;
    int king[2] = {3,4};
    int kingSize = 2;
    int* returnSize = &tmp;
	int tmp2 = 1;
	int* tmp3 = &tmp2;
    int** returnColumnSizes = &tmp3;
    int **res;
    res = queensAttacktheKing((int**)queens, queensSize, queensColSize, (int*)king, kingSize, returnSize, returnColumnSizes);
    int* tmp4 = (int*)res;
    for (int i=0; i<*returnSize; i++){
        printf("[%d, %d]\n", (*(tmp4+i*2+0)), (*(tmp4+i*2+1)));
    }
    free(res);
    return 0;
}