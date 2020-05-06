class Solution {
    private int sum(int[] tmp){
        int res = 0;
        for(int i=0; i<tmp.length; i++){
            res += tmp[i];
        }
        return res;
    }

    public int canCompleteCircuit(int[] gas, int[] cost) {
        if(sum(gas)<sum(cost)){
            return -1;
        }
        
        int start = 0;
        int remain = 0;
        for(int i=0; i<gas.length; i++){
            remain += (gas[i] - cost[i]);
            if(remain < 0){
                start = i+1;
                remain = 0;
            }
        }

        return start;
    }
}