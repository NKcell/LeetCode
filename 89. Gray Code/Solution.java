import java.util.ArrayList;

class Solution {
    public List<Integer> grayCode(int n) {
        ArrayList<Integer> res = new ArrayList<>() ;
        res.add(0);
        for(int i=0; i<n; i++){
            int tmp = res.size();
            for(int j = tmp-1; j>=0; j--){
                res.add(res.get(j)+tmp);
            }
        }
        return res;
    }
}