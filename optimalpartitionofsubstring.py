class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        subCount = 0
        subMem=[]
        step=0
        fin = len(s)
        for i in s:
            step +=1
            if i in subMem:
                subCount += 1
                subMem=[i]
            else:
                subMem.append(i)
            if  step == fin :
                subCount +=1
        return subCount