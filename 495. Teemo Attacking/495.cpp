class Solution {
public:
    int findPoisonedDuration(vector<int>& timeSeries, int duration)     {
        int res = 0;
        for (int i=1; i<timeSeries.size(); i++){
            if(timeSeries[i-1]+duration<timeSeries[i]){
                res += duration;
            }else{
                res += (timeSeries[i]-timeSeries[i-1]);
            }
        }
        if (timeSeries.size()>=1){
            res += duration;
        }
        return res;
    }
};