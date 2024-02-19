class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        counter = 1 


        for i in flowerbed:
            if i == 0:
                counter +=1
            else:
                counter = 0

            if counter == 3:
                counter = 1
                n = n-1
                 
          
            if n ==0:
                return True
        
        if counter==2 and n == 1:
            return True
        else :
            return False
    
        