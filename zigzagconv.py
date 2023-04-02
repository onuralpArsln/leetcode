# For each row, we can get the characters in that row by starting at the first character of the string
# and incrementing by the number of characters between two adjacent characters in that row.
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

# Creating an array of strings, each string is a row of the zigzag pattern.
#         For example, if numRows = 4, then resArr = ['PAYPALISHIRING', 'APLSIIG', 'YIR', 'P']
#         The first string is the first row of the zigzag pattern, the second string is the second row
# of the zigzag pattern, etc.
#         The first string is created by starting at the first character of the string and
# incrementing by the number of characters between two adjacent characters in that row.
#         The second string is created by starting at the second character of the string and
# incrementing by the number of characters between two adjacent characters in that row.
#         The third string is created by starting at the third character of the string and
# incrementing by the number of characters between two adjacent characters in that row.
#         The fourth string is created by starting at the fourth character of the string and
# incrementing by the number of characters between two adjacent characters in that row.
#         The fifth string is created by starting at the fifth character of the string and
# incrementing

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
         