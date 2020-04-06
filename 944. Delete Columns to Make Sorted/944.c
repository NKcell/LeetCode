int minDeletionSize(char ** A, int ASize){
    int len = strlen(*A);
    int count = 0;
    for (int i=0; i<len; i++){
        for (int j=1; j<ASize; j++){
            if(A[j-1][i] > A[j][i]){
                count++;
                break;
            }
        }
    }
    return count;
}