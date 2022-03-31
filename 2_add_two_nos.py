class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c=dummy=ListNode()
        
        carry=0
        while l1 or l2:
            if l1:
                l1_val=l1.val
            else:
                l1_val=0
            if l2:
                l2_val=l2.val
            else:
                l2_val=0
                
            sum_=l1_val+l2_val+carry
            
            c.next=ListNode(sum_%10)
            c=c.next
            carry=sum_//10
            
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        if carry:
            carry=ListNode(carry)
            c.next=carry
        return dummy.next
                
            
        
            
        
            
                
        
