# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        memNode = 0
        memVal = 0 
        currentNode = head
        if not head:
            return head

        while currentNode.next:
            memNode=currentNode
            memVal=currentNode.val
            currentNode = currentNode.next
            while currentNode.val == memVal:
                memNode.next=currentNode.next
                if(currentNode.next):
                    currentNode = currentNode.next
                else:
                        break
               


        return head
