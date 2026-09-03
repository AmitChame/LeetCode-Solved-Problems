class Solution(object):
    def uniformArray(self, nums1):
        minimum = min(nums1)
        if minimum % 2 == 1:
            return True
        return all(x % 2 == 0 for x in nums1)
        