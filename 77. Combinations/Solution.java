import java.util.ArrayList;
import java.util.List;

class Solution {
    ArrayList<List<Integer>> res = new ArrayList<>();

    public List<List<Integer>> combine(int n, int k) {
        ArrayList<Integer> nums = new ArrayList<>();
        for (int i=1; i<=n; i++){
            nums.add(i);
        }
        dfs(k, new ArrayList<Integer>(), nums);
        return res;
    }

    private void dfs(int n, ArrayList<Integer> tmp, ArrayList<Integer> nums){
        if (nums.size() < n){
            return;
        }

        if (n == 0){
            res.add(tmp);
        }

        for (int i=0; i<nums.size(); i++){
            if (nums.size()-i < n){
                break;
            }

            ArrayList<Integer> newtmp = new ArrayList<>(tmp);
            newtmp.add(nums.get(i));

            ArrayList<Integer> newnums = new ArrayList<>(nums.subList(i+1, nums.size()));

            dfs(n-1, newtmp, newnums);
        }
    }
}