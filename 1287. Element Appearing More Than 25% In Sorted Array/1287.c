int findSpecialInteger(int* arr, int arrSize){
    int count = 1;
    int flag = arrSize/4 + 1;
    for (int i=1; i<arrSize; i++){
        if (count>flag){
            return arr[i-1];
        }

        if (arr[i] == arr[i-1]){
            count++;
        }else{
            count = 1;
        }
    }
    return arr[arrSize-1];
}