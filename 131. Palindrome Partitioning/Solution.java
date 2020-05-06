class Solution {
    ArrayList<List<String>> res = new ArrayList<>();

    public List<List<String>> partition(String s) {
        dfs(s, new ArrayList<String>());
        return res;
    }

    private boolean ispar(String s){
        int l = 0;
        int r = s.length()-1;

        while(l<r){
            if(s.charAt(l) != s.charAt(r)){
                return false;
            }
            l ++;
            r --;
        }

        return true;
    }

    private void dfs(String s, ArrayList<String> tmp){
        if(s.length() == 0){
            res.add(tmp);
            return;
        }

        for(int i=0; i<s.length(); i++){
            if (ispar(s.substring(0, i+1))){
                ArrayList<String> newtmp = new ArrayList<>(tmp);
                newtmp.add(s.substring(0, i+1));
                dfs(s.substring(i+1), newtmp);
            }
        }
    }
}