#include <stdio.h>
#include <string.h>

char isLetter(char l){
    if ((l>0x40&&l<0x5b)||(l>0x60&&l<0x7b)){
        return 1;
    }
    return 0;
}

char * reverseOnlyLetters(char * S){
    int lst = strlen(S)-1;
    int pre = 0;

    while (lst>pre){
        char flag = 0;
        if (isLetter(*(S+lst))==0){
            lst--;
            flag = 1;
        }
        if (isLetter(*(S+pre))==0){
            pre++;
            flag = 1;
        }
        if (flag == 1){
            continue;
        }

        char tmp = *(S+lst);
        *(S+lst) = *(S+pre);
        *(S+pre) = tmp;
        lst--;
        pre++;
    }
    return S;
}

int main(){
    char a[] = {'a','-','b','C','-','d','E','f','-','g','h','I','j', 0x00};
    printf("%s\n", reverseOnlyLetters(a));
    return 0;
}