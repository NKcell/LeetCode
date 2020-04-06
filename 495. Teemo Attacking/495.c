

int findPoisonedDuration(int* timeSeries, int timeSeriesSize, int duration){
    int res = 0;
    for(int i=1; i<timeSeriesSize; i++){
        if(*(timeSeries+i-1)+duration < *(timeSeries+i)){
            res += duration;
        }else{
            res += (*(timeSeries+i) - *(timeSeries+i-1));
        }
    }
    if (timeSeriesSize>=1){
        res += duration;
    }
    return res;
}

