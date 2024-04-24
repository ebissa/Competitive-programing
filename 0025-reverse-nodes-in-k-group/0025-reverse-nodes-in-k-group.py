# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(None)
        dummy.next=head
        current=head
        starting=dummy
        count=0
        while current:
            count+=1
            if count==k:
                ending=starting.next 
                temp1=current.next
                prev=starting
                cur=prev.next
                while count>0:
                    temp=cur.next
                    cur.next=prev
                    prev=cur
                    cur=temp
                    count-=1
                starting.next=current
                current=temp1
                ending.next=current
                starting=ending
            else:
                current=current.next
        return dummy.next
                


        