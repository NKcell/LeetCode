int* diStringMatch(char * S, int* returnSize){
    int* res = (int*)malloc(sizeof(int)*(strlen(S)+1));
    *res = 0;
    int max = 0;
    int min = 0;
    for (int i=0; i < strlen(S); i++){
        if (S[i] == 'I'){
            max++;
            *(res+i+1) = max;
        }else{
            min--;
            *(res+i+1) = min;
        }
    }

    for (int j=0; j<strlen(S)+1; j++){
        *(res+j) = *(res+j) - min;
    }

    *returnSize = strlen(S)+1;
    return res;
}

int* diStringMatch2(char* S, int* returnSize) {
    
    if(S==NULL){
        *returnSize = 0;
        return NULL;
    }
    
    int cur_hi = strlen(S);
    int cur_low = 0;
    
    int* ret = (int*)calloc(cur_hi+1, sizeof(int));
    *returnSize = 0;
    
    for(int i = 0; i< strlen(S); i++){
        if(S[i]=='D'){
            ret[(*returnSize)++] = cur_hi;
            cur_hi--;
        }
        
        if(S[i]=='I'){
            ret[(*returnSize)++] = cur_low;
            cur_low++;
        }
    }

    ret[(*returnSize)++] = cur_low;
    
    return ret;
}