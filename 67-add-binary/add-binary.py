class Solution:
    def addBinary(self, a: str, b: str) -> str:
            val=0
            step=1
            for num in reversed(a) : 
                val+=int(num)*step
                step *=2
            step=1
            for num in reversed(b) : 
                val+=int(num)*step
                step *=2
            return "{0:b}".format(val)


