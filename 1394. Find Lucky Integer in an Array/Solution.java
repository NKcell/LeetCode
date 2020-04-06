class Solution {
    public int findLucky(int[] arr) {
        HashMap<Integer, Integer> myMap = new HashMap();
        for(int i=0; i<arr.length; i++){
            Integer tmp = myMap.get(arr[i]);
            if(tmp == null){
                myMap.put(arr[i], 1);
            }else{
                myMap.put(arr[i], tmp+1);
            }
        }

        int res = -1;

        Iterator iter = myMap.entrySet().iterator();
        while(iter.hasNext()){
            Map.Entry entry = (Map.Entry)iter.next();
            Integer key = (Integer)entry.getKey();
            Integer val = (Integer)entry.getValue();
            if (key-val == 0){
                if (val-res>0){
                    res = val;
                }
            }
        }

        return res;
    }
}