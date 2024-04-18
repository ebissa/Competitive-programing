# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        before=ListNode(None)
        dummy=before
        leftover=0
        while l1 and l2:
            sums=l1.val+l2.val+leftover
            if sums>=10:
                remainder=sums%10
                leftover=1
            else:
                remainder=sums
                leftover=0
            new=ListNode(remainder)
            before.next=new
            before=new
            l1=l1.next
            l2=l2.next
        while l1:
            sums=l1.val+leftover
            if sums>=10:
                remainder=sums%10
                leftover=1
            else:
                remainder=sums
                leftover=0
            new=ListNode(remainder)
            before.next=new
            before=new
            l1=l1.next
        while l2:
            sums=l2.val+leftover
            if sums>=10:
                remainder=sums%10
                leftover=1
            else:
                remainder=sums
                leftover=0
            new=ListNode(remainder)
            before.next=new
            before=new
            l2=l2.next
        if leftover>0:
            new=ListNode(leftover)
            before.next=new
            before=new
        before.next=None
            
        return dummy.next
            
            
        
            
        