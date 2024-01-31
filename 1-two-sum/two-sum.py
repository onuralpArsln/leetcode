class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         
        hashMap={}

        for  index,value in enumerate(nums):
            req = target - value 

            if req in hashMap:
                return [index, hashMap[req]  ]
            
            else:
                hashMap[value] = index

            

