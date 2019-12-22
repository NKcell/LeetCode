#include <stdio.h>
#include <stdlib.h>
#include<string.h>
#include <cstdlib>

int countServers(int grid[][2] , int gridSize, int* gridColSize){
    int *col = (int *)malloc(sizeof(int)*(*gridColSize));
    int *row = (int *)malloc(sizeof(int)*(gridSize));

    memset(col, 0, sizeof(int)*(*gridColSize));
    memset(row, 0, sizeof(int)*(gridSize));

    for(int i=0; i<*gridColSize; i++){
        int count = 0;
        for(int j=0; j<gridSize; j++){
            if (grid[j][i] == 1){
                count ++;
            }
        }
        if(count>1){
            col[i] = 1;
        }
    }

    for(int i=0; i<gridSize; i++){
        int count = 0;
        for(int j=0; j<*gridColSize; j++){
            if (grid[i][j] == 1){
                count ++;
            }
        }
        if(count>1){
            row[i] = 1;
        }
    }

    int count = 0;
    for(int i=0; i<*gridColSize; i++){
        for(int j=0; j<gridSize; j++){
            if (grid[j][i] == 1){
                if (col[i]==1 || row[j]==1){
                    count++;
                }
            }
        }
    }

    free(col);
    free(row);
    return count;
}

int main(){
    int grid[2][2] = {{1,0},{1,1}};
    int tmp = 2;
    int* gridColSize = &tmp;

    printf("%d\n",countServers(grid, 2, gridColSize));
    return 0;
}