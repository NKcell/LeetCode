int sum(int* tmp, int size){
    int res = 0;
    for(int i=0; i<size; i++){
        res += *(tmp+i);
    }
    return res;
}

int canCompleteCircuit(int* gas, int gasSize, int* cost, int costSize){
    if (sum(gas, gasSize) < sum(cost, costSize)){
        return -1;
    }

    int start = 0;
    int remain = 0;

    for(int i=0; i<gasSize; i++){
        remain += (*(gas+i) - *(cost+i));
        if(remain<0){
            start = i+1;
            remain = 0;
        }
    }

    return start;
}