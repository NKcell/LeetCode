import java.util.*;

class Solution {
    public List<String> letterCombinations(String digits) {
        if (digits.length() == 0){
            return new ArrayList<String>();
        }

        HashMap<Character, String> myMap = new HashMap<>();
        myMap.put('2', "abc");
        myMap.put('3', "def");
        myMap.put('4', "ghi");
        myMap.put('5', "jkl");
        myMap.put('6', "mno");
        myMap.put('7', "pqrs");
        myMap.put('8', "tuv");
        myMap.put('9', "wxyz");

        ArrayList<String> res = new ArrayList<>();

        res.add("");

        for(int i=0; i<digits.length(); i++){
            ArrayList<String> newres = new ArrayList<>();
            while(res.size() != 0){
                String tmp = res.remove(0);
                for (int j=0; j<myMap.get(digits.charAt(i)).length(); j++){
                    newres.add(tmp+myMap.get(digits.charAt(i)).charAt(j));
                }
            }
            res = newres;
        }

        return res;
    }
}