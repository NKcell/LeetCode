

char * reformat(char * s){
    int slen = strlen(s);
    char* digit = (char*)malloc(slen);
    memset(digit, 0, slen);
    int digitlen = 0;
    char* letter = (char*)malloc(slen);
    int letterlen = 0;
    memset(letter, 0, slen);

    char* res = (char*)malloc(slen+1);
    memset(res, 0, slen+1);

    while (*s != 0){
        if (*s>='0' && *s<='9'){
            *(digit+digitlen) = *s;
            digitlen++;
        } else{
            *(letter+letterlen) = *s;
            letterlen++;
        }
        s ++;
    }

    int tmp = digitlen - letterlen;
    if (tmp>1 || tmp<-1){
        return "";
    }

    if(digitlen>letterlen){
        for(int i=0; i<letterlen; i++){
            *(res+i*2) = *(digit+i);
            *(res+i*2+1)=*(letter+i);
        }
        *(res+slen-1) = *(digit+digitlen-1);
    }else if(digitlen<letterlen){
        for(int i=0; i<digitlen; i++){
            *(res+i*2) = *(letter+i);
            *(res+i*2+1)=*(digit+i);
        }
        *(res+slen-1) = *(letter+letterlen-1);
    }else{
        for(int i=0; i<digitlen; i++){
            *(res+i*2) = *(letter+i);
            *(res+i*2+1)=*(digit+i);
        }
    }
    return res;
}