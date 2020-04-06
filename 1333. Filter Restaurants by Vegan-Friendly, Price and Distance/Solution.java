class Solution {
    public List<Integer> filterRestaurants(int[][] restaurants, int veganFriendly, int maxPrice, int maxDistance) {
        ArrayList<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>>();

        for (int i=0; i<restaurants.length; i++){
            if (veganFriendly == 1){
                if(restaurants[i][2]==1 && restaurants[i][3]<=maxPrice && restaurants[i][4]<=maxDistance){
                    ArrayList<Integer> tmp = new ArrayList<Integer>();
                    tmp.add(restaurants[i][0]);
                    tmp.add(restaurants[i][1]);
                    res.add(tmp);
                }
            }else{
                if(restaurants[i][3]<=maxPrice && restaurants[i][4]<=maxDistance){
                    ArrayList<Integer> tmp = new ArrayList<Integer>();
                    tmp.add(restaurants[i][0]);
                    tmp.add(restaurants[i][1]);
                    res.add(tmp);
                }
            }
        }

        Collections.sort(res, new Comparator<List<Integer>>(){
            public int compare(List<Integer> a, List<Integer> b){
                if (a.get(1)-b.get(1) == 0){ // 这里不要直接用==，对象==比较地址...
                    return b.get(0)-a.get(0);
                }else{
                    return b.get(1)-a.get(1);
                }
            }
        });

        List<Integer> l = new ArrayList<Integer>();

        for (int i=0; i<res.size(); i++){
            l.add(res.get(i).get(0));
        }

        return l;
    }
}

// class Solution {
//     public List<Integer> filterRestaurants(int[][] restaurants, int veganFriendly, int maxPrice, int maxDistance) {
//         List<int[]> list = new ArrayList<>();
//         for (int[] restaurant : restaurants) {
//             if (((veganFriendly == 1 && restaurant[2] == 1) || veganFriendly == 0)
//             && restaurant[3] <= maxPrice && restaurant[4] <= maxDistance) {
//                 list.add(restaurant);
//             }
//         }
//         Collections.sort(list, (a, b) -> b[1] - a[1] == 0 ? b[0] - a[0] : b[1] - a[1]);
//         return list.stream().map(restaurant -> restaurant[0]).collect(Collectors.toList());
//     }
// }