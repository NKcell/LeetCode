import java.util.*;

class Solution {
    ArrayList<String> res = new ArrayList<>();

    public List<String> generateParenthesis(int n) {
        if (n == 0){
            return res;
        }

        int r = 0;
        int l = n;

        dfs("", r, l, 2*n);

        return res;
    }

    private void dfs(String tmpStr, int r, int l, int n){
        if (tmpStr.length() == n){
            res.add(tmpStr);
        }

        if (l != 0){
            dfs(tmpStr+"(", r+1, l-1, n);
        }
        if (r != 0){
            dfs(tmpStr+")", r-1, l, n);
        }
    }
}