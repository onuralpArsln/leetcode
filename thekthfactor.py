class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        factors = []
        for i in range(n):
            a = i+1
            if n % a ==0:
                factors.append(a)

        if len(factors) > k-1:
            return factors[k-1]
        else:
            return -1
