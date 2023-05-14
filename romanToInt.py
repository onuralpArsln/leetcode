s = "III"

def charVal(s):
            if s =="I":
                return 1
            elif s =="V":
                return 5
            elif s=="X":
                return 10
            elif s=="L":
                return 50
            elif s=="C":
                return 100
            elif s=="D":
                return 500
            else:
                return 1000

s=s[::-1]

for i in range(len(s)):
            if i == 0 :
                result = charVal(s[i])
            else:
                lastVal = charVal(s[i-1])
                currentVal = charVal(s[i])
                if lastVal>currentVal:
                    result=result-currentVal
                else:
                    result += currentVal

print(result) 




"""


instead of using a function to determine the value a dictonary speeds up the detection time 

class Solution(object):
    def romanToInt(self, s):
       
        convert = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        if len(s) == 0:
            return 0

        if len(s) == 1:
            return convert[s[0]]

        total = 0
        for i in range(len(s)-1):
            if convert[s[i]] < convert[s[i+1]]:
                total -= convert[s[i]]
            else:
                total += convert[s[i]]

        total += convert[s[len(s)-1]]

        return total


"""