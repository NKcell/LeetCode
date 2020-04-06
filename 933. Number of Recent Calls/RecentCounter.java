class RecentCounter {

    ArrayList<Integer> res = new ArrayList<Integer>();

    public RecentCounter() {

    }

    public int ping(int t) {

        while (res.size()>0){
            if ((t - res.get(0)) > 3000){
                res.remove(0);
            }else{
                break;
            }
        }

        res.add(t);
        //System.out.println(res);
        return res.size();
    }
}

//  List<Integer> list;

//     public RecentCounter() {
//         list = new ArrayList<>();
//     }
    
//     public int ping(int t) {
//         list.add(t);
//         int index = Collections.binarySearch(list, t - 3000); // search the index of t - 3000.
//         if (index < 0) { index = ~index; } // if t - 3000 is not in list, use the index of the ceiling of t - 3000.
//         return list.size() - index;
//     }

// Queue<Integer> q;

//     public RecentCounter() {
//         q = new LinkedList<>();
//     }
    
//     public int ping(int t) {
//         q.offer(t);
//         while (q.peek() < t - 3000) { q.poll(); }
//         return q.size();
//     }