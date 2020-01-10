char * removeDuplicates(char * S){
    char* res = (char*)malloc(strlen(S));
    memset(res, 0, strlen(S));
    int index = 0;
    for(int i=0; i<strlen(S); i++){
        if (index==0){
            *(res+index) = *(S+i);
            index++;
        }else{
            if (*(res+index-1) == *(S+i)){
                *(res+index-1) = 0;
                index--;
            }else{
                *(res+index) = *(S+i);
                index++;
            }
        }
    }
    return res;
}