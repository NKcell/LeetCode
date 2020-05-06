class Solution {
    public int numDecodings(String s) {
        if (s.length() == 0){
            return 0;
        }
        int v = 0;
        int w = 1;
        char p = '0';
        //String[] ssplit = s.split("");

        for(int i=0; i<s.length(); i++){
            int tmp = 0;
            if (s.charAt(i) != '0'){
                tmp += w;
            }
            int shi = p-'0';
            int ge = s.charAt(i)-'0';
            int value = shi*10 + ge;
            if(value>9 && value<27){
                tmp += v;
            }

            v = w;
            w = tmp;
            p = s.charAt(i);
        }

        return w;
    }
}