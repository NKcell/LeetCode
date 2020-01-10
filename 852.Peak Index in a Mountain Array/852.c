int peakIndexInMountainArray(int* A, int ASize){
    int start = 0;
    int end = ASize-1;
    while(start<=end){
        int mid = (start+end)/2;
        if (*(A+mid)>*(A+mid+1) && *(A+mid)>*(A+mid-1)){
            return mid;
        }
        if (*(A+mid)>*(A+mid-1)){
            start = mid+1;
        }else{
            end = mid-1;
        }
    }
    return 0;
}