bool backspaceCompare(char * S, char * T){
    char* res1 = (char*)malloc(strlen(S)+1);
    memset(res1, 0, strlen(S)+1);
    int index = -1;
    for(int i=0; i<strlen(S); i++){
        if (*(S+i) != '#'){
			index++;
            *(res1+index) = *(S+i);
        }else if(index == -1)
        {
            continue;
        }else{
            *(res1+index) = 0;
			index --;
        }  
    }

    char* res2 = (char*)malloc(strlen(T)+1);
    memset(res2, 0, strlen(T)+1);
    index = -1;
    for(int i=0; i<strlen(T); i++){
        if (*(T+i) != '#'){
			index++;
            *(res2+index) = *(T+i);
        }else if(index == -1)
        {
            continue;
        }else{
            *(res2+index) = 0;
			index --;
        }  
    }

    if (strcmp(res1, res2) == 0){
        return true;
    }
    return false;
}