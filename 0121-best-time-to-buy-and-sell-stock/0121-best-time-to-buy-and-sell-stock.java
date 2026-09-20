class Solution {
    public int maxProfit(int[] prices) {
        int minprice=prices[0];
        int maxprofit=0;
        for(int i=1;i<prices.length;i++){
            if(prices[i]<minprice){
                minprice=prices[i];
            }
            int curr=prices[i]-minprice;
            if(curr>maxprofit){
                maxprofit=curr;
            }

        }
        return maxprofit;

    }
}