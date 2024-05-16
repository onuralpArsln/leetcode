class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        run = 2 * max(len(word1) , len(word2))
        res =""
        pointer1 = 0
        pointer2 = 0

        for i in range(run):
            try:
                if i%2==0:
                    res += word1[pointer1]
                    pointer1 +=1
                else:
                    res += word2[pointer2]
                    pointer2 +=1
            except:
                a = 0 

        return res 



        

        