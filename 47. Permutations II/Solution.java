class Solution {
    List<List<Integer>> res = new ArrayList<>();
    public List<List<Integer>> permuteUnique(int[] nums) {
        Arrays.sort(nums);
        ArrayList<Integer> mynums = new ArrayList<>();
        
        for(int i=0; i<nums.length; i++){
            mynums.add(nums[i]);
        }
        ArrayList<Integer> tmp = new ArrayList<>();
        dfs(mynums, tmp);

        return res;
    }

    private void dfs(ArrayList<Integer> nums, ArrayList<Integer> tmp){
        if (nums.size() == 0){
            res.add(tmp);
            return;
        }
        int pre=0;
        for (int i=0; i<nums.size(); i++){
            
            ArrayList<Integer> newtmp = new ArrayList<>(tmp);
            ArrayList<Integer> newnums = new ArrayList<>(nums);
            if (i == 0){
                pre = nums.get(0);
                newtmp.add(pre);
                newnums.remove(i);
                dfs(newnums, newtmp);
            }else{
                if (nums.get(i) == pre){
                    continue;
                }else{
                    pre = nums.get(i);
                    newtmp.add(pre);
                    newnums.remove(i);
                    dfs(newnums, newtmp);
                }
            }
        }
    }
}