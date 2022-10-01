class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head 
    
        while temp.next is not None:
            if temp.next.next is not None:
                temp = temp.next.next
            else:
                temp = temp.next 
            
            head = head.next 
            
        return head
