class ProductOfNumbers {
    private ArrayList<int> myList;

    public ProductOfNumbers() {
        myList = new ArrayList();
        myList.add(1);
    }
    
    public void add(int num) {
        if (num == 0){
            myList.clear();
            myList.add(1);
        }else{
            myList.add(myList.get(myList.size()-1)*num);
        }
    }
    
    public int getProduct(int k) {
        if(k>=myList.size()){
            return 0;
        }else{
            return myList.get(myList.size()-1)/myList.get(myList.size()-k-1);
        }
    }
}