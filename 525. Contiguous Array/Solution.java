class Solution {
    public int findMaxLength(int[] nums) {
        int count = 0;
        int maxLength = 0;
        HashMap<Integer, Integer> myMap = new HashMap<Integer, Integer>();

        myMap.put(0,0);

        for (int i=0; i<nums.length; i++){
            if (nums[i] == 0){
                count--;
            }else{
                count++;
            }

            int j = i+1;

            Integer tmp = myMap.get(count);
            if(tmp == null){
                myMap.put(count, j);
            }else{
                maxLength = Math.max(maxLength, j-tmp);
            }
        }

        return maxLength;
    }
}