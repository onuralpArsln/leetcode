class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums = ["0","1","2","3","4","5","6","7","8","9"]
        accepted = [" ","-","+","0","1","2","3","4","5","6","7","8","9"]

        isMinus= False
        cancel= False
        counting = False
        s = s.strip()
        res = ""
        for i in s:
            if i not in accepted:
                break
            else:
                if i == "-" and not counting:
                    isMinus = True
                if i == "+" or i =="-" or i ==" ":
                    if cancel or counting :
                        break
                    cancel = True

                elif i in nums:

                    counting = True

                    res += i
                    

        
        try:
            res = int(res)
        except:
            res = 0

        if isMinus:
            res *= -1

        if res > 2**31 - 1:
            print("ilk")
            return 2**31 - 1
        elif res < -2**31:
            print("iki")
            return -2**31
        else:
            print("uc")
            return res 




            
        

        


        
        return int(res) if res != "" else 0