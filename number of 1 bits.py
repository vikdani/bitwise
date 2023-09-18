class Solution(object):
    def hasAlternatingBits(self, n):
        if not n:
            return True
        num = n ^ (n>>1)
        return not num & (num+1)
        """
        :type n: int
        :rtype: bool
        """