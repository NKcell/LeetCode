bool isPerfectSquare(int num){
    int start = 0;
    int end = num > 46340 ? 46340 : num;

    while(start<=end){
        int mid = (start+end)/2;
        int tmp = mid*mid;
        if(tmp == num){
            return true;
        }
        if (tmp>num){
            end = mid-1;
        }else{
            start = mid+1;
        }
    }

    return false;
}