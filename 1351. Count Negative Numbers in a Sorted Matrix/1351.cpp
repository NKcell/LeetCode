class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int count = 0;
        int myLen = grid[0].size();
        for (int i=0; i<grid.size(); i++){
            for (int j=0; j<myLen; j++){
                if (grid[i][j]<0){
                    count += (myLen-j);
                    break;
                }
            }
        }
        return count;
    }
};