# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        maxmum=float("-inf")
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        first,second=head,slow.next
        prev=None
        while second:
            temp=second.next
            second.next=prev
            prev=second
            second=temp
        while prev:
            sums=head.val+prev.val
            maxmum=max(maxmum,sums)
            prev=prev.next
            head=head.next
        return maxmum
        
