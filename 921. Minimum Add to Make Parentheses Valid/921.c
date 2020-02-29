int minAddToMakeValid(char * S){
    char* res = (char*)malloc(sizeof(char)*strlen(S));
    int index = 0;
    for (int i=0; i<strlen(S); i++){
        if (*(S+i)=='('){
            *(res+index) = '(';
            index ++;   
        }else{
            if (index == 0){
                *(res+index) = ')';
                index ++;
            }else if(*(res+index-1) == '('){
                index --;
            }
            else{
                 *(res+index) = ')';
                index ++;
            }
        }
    }
    free(res);
    return index;
}