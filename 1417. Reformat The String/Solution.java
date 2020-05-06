import java.util.ArrayList;

class Solution {
    public String reformat(String s) {
        ArrayList<String> letter = new ArrayList<>();
        ArrayList<String> digit = new ArrayList<>();
        String res = "";

        for(int i=0; i<s.length(); i++){
            if(s.charAt(i)<='9' && s.charAt(i)>='0'){
                digit.add(""+s.charAt(i));
            }else{
                letter.add(""+s.charAt(i));
            }
        }

        int tmp = digit.size() - letter.size();
        if(tmp>1 || tmp<-1){
            return "";
        }

        if(tmp>0){
            for(int i=0; i<letter.size(); i++){
                res += digit.get(i);
                res += letter.get(i);
            }
            res += digit.get(letter.size());
        }else if(tmp<0){
            for(int i=0; i<digit.size(); i++){
                res += letter.get(i);
                res += digit.get(i);
            }
            res += letter.get(digit.size());
        }else{
            for(int i=0; i<letter.size(); i++){
                res += digit.get(i);
                res += letter.get(i);
            }
        }

        return res;
    }
}