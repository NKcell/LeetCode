class Solution {
    public int findMinDifference(List<String> timePoints) {
        int len = timePoints.size();

        int[] timeList = new int[len];

        for(int i=0; i<len; i++){
            String[] hm = timePoints.get(i).split(":");
            try {
                int hour = Integer.parseInt(hm[0]);
                int minute = Integer.parseInt(hm[1]);
                timeList[i] = 60*hour+minute;
            } catch (NumberFormatException e) {
                e.printStackTrace();
            }
        }
        Arrays.sort(timeList);
        int minValue = timeList[1]-timeList[0];

        for (int i=2; i<len; i++){
            int tmp = timeList[i]-timeList[i-1];
            if (tmp<minValue){
                minValue = tmp;
            }
        }

        int tmp = 24*60+timeList[0]-timeList[len-1];
        if (tmp<minValue){
            return tmp;
        }
        return minValue;
    }
}

// public class Solution {
//     public int findMinDifference(List<String> timePoints) {
//         int mm = Integer.MAX_VALUE;
//         List<Integer> time = new ArrayList<>();
        
//         for(int i = 0; i < timePoints.size(); i++){
//             Integer h = Integer.valueOf(timePoints.get(i).substring(0, 2));
//             time.add(60 * h + Integer.valueOf(timePoints.get(i).substring(3, 5)));
//         }
        
//         Collections.sort(time, (Integer a, Integer b) -> a - b);
        
//         for(int i = 1; i < time.size(); i++){
//             System.out.println(time.get(i));
//             mm = Math.min(mm, time.get(i) - time.get(i-1));
//         }
        
//         int corner = time.get(0) + (1440 - time.get(time.size()-1));
//         return Math.min(mm, corner);
//     }
// }