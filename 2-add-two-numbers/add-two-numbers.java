/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
        ListNode  result = new ListNode();
        int holder  = 0;
        ListNode processing = result;

        if(l1.val+l2.val > 9){
            result.val = l1.val + l2.val - 10;
            holder=1;
        }else{result.val = l1.val + l2.val;}
        

        while (l1.next!=null && l2.next!=null){
            l1 = l1.next;
            l2=l2.next;
            ListNode current = new ListNode();

            if(l1.val+l2.val + holder > 9){
                current.val = l1.val + l2.val + holder - 10;
                holder=1;
            }else{current.val = l1.val + l2.val + holder; holder=0;}
            processing.next=current;
            processing=current;

        }

            while (l1.next!=null){
            l1 = l1.next;
             ListNode current = new ListNode();

            if(l1.val + holder > 9){
                current.val = l1.val  + holder - 10;
                holder=1;
            }else{current.val = l1.val  + holder; holder=0;}
                    processing.next=current;
            processing=current;

        }  

    
            while (l2.next!=null){
            l2 = l2.next;
             ListNode current = new ListNode();

            if(l2.val + holder > 9){
                current.val = l2.val  + holder - 10;
                holder=1;
            }else{current.val = l2.val  + holder; holder=0;}
                           processing.next=current;
            processing=current;

        } 
        if (holder==1){
            ListNode current = new ListNode(1);
            processing.next=current;
            processing=current;

        }
return result;
        }
        
    }
