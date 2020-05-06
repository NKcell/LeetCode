class Solution {
    public String destCity(List<List<String>> paths) {
        HashMap<String, Integer> res=new HashMap();

        for(int i=0; i< paths.size(); i++){
            Integer tmp = res.get(paths.get(i).get(0));
            if (tmp == null){
                res.put(paths.get(i).get(0), 0);
            }else{
                res.remove(paths.get(i).get(0));
            }

            tmp = res.get(paths.get(i).get(1));
            if (tmp == null){
                res.put(paths.get(i).get(1), 1);
            }else{
                res.remove(paths.get(i).get(1));
            }
        }

        for (Map.Entry<String, Integer> entry : res.entrySet()) {
            if (entry.getValue() == 1){
                return entry.getKey();
            }
        }
        
        return "";
    }
}