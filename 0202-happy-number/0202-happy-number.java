class Solution {
    public boolean isHappy(int n) {
        int fast=n;
        int slow=n;
        do{
            slow=findsqr(slow);
            fast=findsqr(findsqr(fast));
        }while(fast!=slow);
        if(slow==1){
            return true;
        }        
        return false;
    }
    public int findsqr(int n){
        int ans=0;
        int rem=0;
        while(n>0){
            rem=n%10;
            ans+=rem*rem;
            n=n/10;
        }
        return ans;
    }
}