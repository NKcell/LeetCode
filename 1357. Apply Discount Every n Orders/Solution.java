class Cashier {
    int n;
    int people;
    HashMap<Integer, Integer> myMap;
    int discount;

    public Cashier(int n, int discount, int[] products, int[] prices) {
        this.n = n;
        this.discount = discount;
        this.myMap = new HashMap();
        for(int i=0; i<products.length; i++){
            myMap.put(products[i], prices[i]);
        }
    }
    
    public double getBill(int[] product, int[] amount) {
        this.people++;
        double sum = 0;
        if(this.n == this.people){
            this.people = 0;
            for(int i=0; i<product.length; i++){
                sum += this.myMap.get(product[i])*amount[i];
            }
            sum *= (1-discount/100.0);
        }else{
            for(int i=0; i<product.length; i++){
                sum += this.myMap.get(product[i])*amount[i];
            }
        }
        return sum;
    }
}