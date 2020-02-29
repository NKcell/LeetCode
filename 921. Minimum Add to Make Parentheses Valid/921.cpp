class Solution {
public:
    int minAddToMakeValid(string S) {
        vector<char> res;
        for(int i=0; i<S.length(); i++){
            if (S[i] == '('){
                res.push_back('(');
            }else{
                if (res.size() == 0){
                    res.push_back(')');
                }else if(res[res.size()-1] == '('){
                    res.pop_back();
                }else{
                    res.push_back(')');
                }
            }
        }
        return res.size();
    }
};