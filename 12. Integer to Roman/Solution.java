class Solution {
    public String intToRoman(int num) {
        int[] value = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] symble = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        String res = "";

        int i = 0;
        while(true){
            if (num == 0){
                return res;
            }
            int tmp = num/value[i];

            for(int j=0; j<tmp; j++){
                res += symble[i];
            }
            
            num = num%value[i];
            i++;
        }
    }
}