class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res=0
        
        for i in range(len(digits)):
            res += digits[-1*(i+1)]*(10**i)
            print(res)

        res += 1
        print(res)
        res = str(res)
        res = list(map(int, str(res)))        
        return res 
