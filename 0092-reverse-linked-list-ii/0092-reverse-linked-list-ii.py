# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev_left = dummy

        for i in range(left - 1):
            prev_left = prev_left.next

        prev_node, current = None, prev_left.next

        for i in range(right - left + 1):
            next_node = current.next
            current.next = prev_node
            prev_node = current
            current = next_node

        prev_left.next.next = current
        prev_left.next = prev_node

        return dummy.next

            