#include <stdio.h>
#include <string.h>

int uniqueMorseRepresentations(char ** words, int wordsSize){
    char res[100][50];
    char* morse[26] = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};

    if (wordsSize == 0){
        return 0;
    }

    for (int i=0; i<wordsSize; i++){
        int tmp = 0;
        int tmp2 = 0;
        while (*(*(words+i)+tmp) != 0x00){
            memcpy(res[i]+tmp2,morse[*(*(words+i)+tmp)-'a'],strlen(morse[*(*(words+i)+tmp)-'a']));
            tmp2 += strlen(morse[*(*(words+i)+tmp)-'a']);
            tmp++;
        }
        res[i][tmp2] = 0x00;
    }

    int count = 1;
    for (int j=1; j<wordsSize; j++){
        char flag = 0;
        for (int k=0; k<j; k++){
            if (strcmp(res[j], res[k])==0){
                flag = 1;
                break;
            }
        }
        if (flag == 0){
            count++;
        }
    }

    return count;
}

int main(){
    char* words[] = {"gin", "zen", "gig", "msg"};
    printf("%d\n", uniqueMorseRepresentations(words, 4));
    return 0;
}