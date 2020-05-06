

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
bool ispar(char* str){
    int l=0;
    int r=strlen(str)-1;

    while(l<r){
        if (*(str+l) != *(str+r)){
            return 0;
        }
        l++;
        r--;
    }
    return 1;
}

void dfs(char**** res, char** tmp, int tmpLen, int* returnSize, int** returnColumnSizes, char* s){
    if(strlen(s) == 0){
        char*** newres = (char***)malloc((*returnSize+1)*sizeof(char**));
        memcpy(newres, *res, *returnSize*sizeof(char**));
        *(newres+*returnSize) = tmp;
        *res = newres;

        int* newreturnColumnSizes = (int*)malloc((*returnSize+1) * sizeof(int));
        memcpy(newreturnColumnSizes, *returnColumnSizes, *returnSize*sizeof(int));
        *(newreturnColumnSizes+*returnSize) = tmpLen;
        *returnColumnSizes = newreturnColumnSizes;

        *returnSize += 1;
        return;
    }

    for(int i=1; i<strlen(s)+1; i++){
        char* tmpstring = (char*)malloc((i+1)*sizeof(char));
        memcpy(tmpstring, s, i);
        *(tmpstring+i) = 0;
        if (ispar(tmpstring)){
            char** newtmp = (char**)malloc((tmpLen+1)*sizeof(char*)); 
            memcpy(newtmp, tmp, tmpLen*sizeof(char*));
            *(newtmp+tmpLen) = tmpstring;

            char* news = (char*)malloc((strlen(s)-i+1)*sizeof(char));
            memcpy(news, s+i, (strlen(s)-i+1));
            dfs(res, newtmp, tmpLen+1, returnSize, returnColumnSizes, news);
            free(news);
        }
    }

    free(tmp);
}

char *** partition(char * s, int* returnSize, int** returnColumnSizes){
    *returnSize = 0;
    *returnColumnSizes = (int*)malloc(0*sizeof(int));
    char*** res = (char***)malloc(0*sizeof(char**));
    char** tmp = (char**)malloc(0*sizeof(char*)); 

    dfs(&res, tmp, 0, returnSize, returnColumnSizes, s);

    return res;
}

