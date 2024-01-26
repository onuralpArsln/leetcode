class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        wordlen = len(needle)


        for index, value in enumerate(haystack):
            if value == needle[0]:
                if  haystack[index:index+wordlen] == needle:
                    
                    return int(index)
        
        return -1
                
