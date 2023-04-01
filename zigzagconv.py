class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        word= s
        resArr = []
        res =''
        arrCount = 2*numRows-2


        for i in range(2*numRows-2):
            resArr.append(word[i::2*numRows-2])
        

        if numRows > 1 :
            res= resArr[0]
       

            for i in range(numRows-2):
                arr1 = i +1
                arr2 = arrCount-1-i
   
                for j in range(len(resArr[arr2])):
                    res = res + resArr[arr1][j]
                    res = res + resArr[arr2][j]
                if len(resArr[arr1]) > len(resArr[arr2]):
                    res = res + resArr[arr1][-1]


            res = res + resArr[numRows-1]
        else:
            res = s

        return res 