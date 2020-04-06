class Solution {
    public List<String> summaryRanges(int[] nums) {
        if (nums.length == 0){
            return new ArrayList<String>();
        }
        
        ArrayList<String> res = new ArrayList();
        int start = nums[0];
        int last = nums[0];

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == last+1){
                last += 1;
            }else{
                if (start == last){
                    String tmp = ""+start;
                    res.add(tmp);
                }else{
                    String tmp = start + "->" + last;
                    res.add(tmp);
                }
                start = nums[i];
                last = start;
            }
        }

        if (start == last){
            String tmp = ""+start;
            res.add(tmp);
        }else{
            String tmp = start + "->" + last;
            res.add(tmp);
        }
        
        return res;
    }
}