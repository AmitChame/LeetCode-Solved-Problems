class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        num=0
        for i in jewels:
            for j in stones:
                if i==j:
                    num=num+1
        return num
