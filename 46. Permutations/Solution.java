class Solution {
    List<List<Integer>> res = new ArrayList<List<Integer>>(); 

    public List<List<Integer>> permute(int[] nums) {
        ArrayList<Integer> mynums = new ArrayList<>();
        for(int i=0; i<nums.length; i++){
            mynums.add(nums[i]);
        }

        dfs(new ArrayList<Integer>(), mynums);

        return res;
    }

    private void dfs(ArrayList<Integer> tmp, ArrayList<Integer> mynums){
        if (mynums.size() == 0){
            res.add(tmp);
        }
        
        for (int i=0; i<mynums.size(); i++){
            ArrayList<Integer> newtmp = new ArrayList<Integer>(tmp);
            ArrayList<Integer> newnums = new ArrayList<>(mynums);
            newtmp.add(mynums.get(i));
            newnums.remove(i);
            dfs(newtmp, newnums);
        }
    }
}