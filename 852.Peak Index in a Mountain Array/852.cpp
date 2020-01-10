class Solution {
public:
    int peakIndexInMountainArray(vector<int>& A) {
        int end = A.size()-1;
		int start = 0;
		while(start<=end){
			int mid = (start+end)/2;
			if(A[mid]>A[mid+1] && A[mid]>A[mid-1]){
				return mid;
			}
			if (A[mid]>A[mid-1]){
				start = mid+1;
			}else{
				end = mid-1;
			}
		}
		return 0;
    }
};