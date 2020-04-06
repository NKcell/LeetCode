class Solution {
    public int numTimesAllBlue(int[] light) {
        int count = 0;
        int maxNum = 1;

        for (int i=0; i<light.length; i++){
            if (light[i]>maxNum){
                maxNum = light[i];
            }

            if (i+1 >= maxNum){
                count++;
            }
        }
        
        return count;
    }
}