int subtractProductAndSum(int n){
    int sum = 0;
    int pro = 1;

    while (n!=0){
        int tmp = n%10;
        sum += tmp;
        pro *= tmp;
        n = n/10;
    }
    
    return pro-sum;
}