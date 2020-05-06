

int numDecodings(char * s){
    if(*s == 0){
        return 0;
    }

    int w = 1;
    int v = 0;
    char p = '0';

    while (*s != 0){
        int tmp = 0;
        if(*s != '0'){
            tmp += w;
        }

        int shi = p-'0';
        int ge = *s-'0';
        int value = shi*10+ge;

        if(value>9 && value<27){
            tmp += v;
        }

        v = w;
        w = tmp;
        p = *s;
        s += 1;
    }

    return w;
}

