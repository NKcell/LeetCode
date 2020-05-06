import java.util.ArrayList;

class Solution {
    public String getPermutation(int n, int k) {
        ArrayList<String> tmp = new ArrayList<>();
        for (int i=1; i<=n; i++){
            tmp.add(Integer.toString(i));
        }
        k --;

        String res = ""; 
        while (n!=0){
            n--;
            int chushu = jie(n);
            int index = k/chushu;
            k = k%chushu;
            res += tmp.get(index);
            tmp.remove(index);
        }

        return res;
    }

    private int jie(int n){
        int res = 1;
        while(n != 0){
            res *= n;
            n--;
        }
        return res;
    }
}