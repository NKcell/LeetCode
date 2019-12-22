#include<string.h>

int minimumSwap(char * s1, char * s2){
    char *res = (char*)malloc(strlen(s1));
    int count = 0;
    for (int i=0; i<strlen(s1); i++){
        if (*(s1+i)!=*(s2+i)){
            *(res+count) = *(s1+i);
            count++;
        }
    }
    if (count%2 != 0){
        return -1;
    }

    int x = 0;
    int y = 0;

    for (int j=0; j<count; j++){
        if (*(res+j) == 'x'){
            x++;
        }else{
            y++;
        }
    }

    free(res);
    
    if (x%2 == 0){
        return x/2+y/2;
    }
    return x/2+y/2+2;
}