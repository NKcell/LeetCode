import java.util.ArrayList;

class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int maxNum = Arrays.stream(candies).max().getAsInt();
        ArrayList<Boolean> res = new ArrayList<>();
        for(int i=0; i<candies.length; i++){
            if(candies[i]+extraCandies >= maxNum){
                res.add(true);
            }else{
                res.add(false);
            }
        }
        return res;
    }
}