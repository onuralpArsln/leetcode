class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        lens=[]

        for s in strs:
            lens.append(len(s))

        lens.sort()
        result = ""

        for i in range(lens[0]):
            letter = strs[0][i]
            for s in strs:
                if s[i] != letter:
                    return result

            result += letter
        
        return result
    


# beats  93.49 % at runtime and 81.61% in memeory