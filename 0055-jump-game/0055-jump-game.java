class Solution {
    public boolean canJump(int[] nums) {
        int lastindex = nums.length - 1;
        int farthest = 0;

        for(int i = 0; i < nums.length; i++) {

            if(i > farthest) {
                return false;
            }

            farthest = Math.max(farthest, i + nums[i]);

            if(farthest >= lastindex) {
                return true;
            }
        }

        return false;
    }
}