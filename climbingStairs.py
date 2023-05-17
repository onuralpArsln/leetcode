class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        import math

        result = 0 
        

        for i in range((n/2)+1):
            result+= math.factorial(n-i)/(math.factorial(n-(2*i))*math.factorial(i))

        return result


"""
runtime
 Beats
96.10%
Memory
13.2 MB
Beats
98.53%
"""