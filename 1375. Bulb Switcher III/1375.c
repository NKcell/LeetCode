int numTimesAllBlue(int* light, int lightSize){
    int count = 0;
    int maxNum = 1;

    for (int i=0; i<lightSize; i++){
        if(*(light+i) > maxNum){
            maxNum = *(light+i);
        }

        if((i+1)>=maxNum){
            count++;
        }
    }

    return count;
}

