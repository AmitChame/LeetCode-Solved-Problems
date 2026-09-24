class Solution {
    public void rotate(int[] nums, int k) {
        
        k=k%nums.length;
        
        int temp[]=new int[nums.length];
        
        for(int i=0;i<nums.length;i++){
            int newindex=(i+k)%nums.length;
            temp[newindex]=nums[i];
        }

        for(int i=0;i<nums.length;i++){
            nums[i]=temp[i];
        }
        
    }
}