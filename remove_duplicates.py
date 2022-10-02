class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head    
        prev=dummy
               
        while head!=None :
            if head.next!=None and head.val==head.next.val:
                while head.next!=None and head.val==head.next.val:
                    head=head.next
                prev.next=head.next
            else:
                prev=prev.next
            head=head.next

        return dummy.next
