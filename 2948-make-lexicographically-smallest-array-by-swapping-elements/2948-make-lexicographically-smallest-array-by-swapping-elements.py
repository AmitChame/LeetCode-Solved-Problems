class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """
        
        n = len(nums)
        
        # Store (value, original_index) and sort by value
        arr = sorted((nums[i], i) for i in range(n))
        
        result = [0] * n
        i = 0
        
        while i < n:
            j = i
            
            # Find all elements belonging to the same group
            while j + 1 < n and arr[j + 1][0] - arr[j][0] <= limit:
                j += 1
            
            # Get indices of this group and sort them
            indices = sorted(arr[k][1] for k in range(i, j + 1))
            
            # Values are already sorted because arr is sorted
            for k in range(len(indices)):
                result[indices[k]] = arr[i + k][0]
            
            i = j + 1
        
        return result