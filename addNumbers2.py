# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = []
        remainder =0
        step=0
        val1 = l1
        num1=0
        force=1
        # convert to number
        while val1 !=None:
            num1+= force * val1.val
            force*=10
            val1=val1.next

        
            

        val2 = l2 
        num2=0
        force=1
        # convert to number
        while val2 !=None:
            num2+= force * val2.val
            force*=10
            val2=val2.next
        
        res = num1+num2


        
        lastNode=None
        initialNode=None
    
        res = str(res)
        res=res[::-1]

        for i in res:
            resNode= ListNode()
            resNode.val=int(i)
            if lastNode!=None:
                lastNode.next=resNode
            lastNode=resNode
            if initialNode==None:
                initialNode=resNode

        return initialNode
        
            

        
            

            

        