"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapper={None:None}
        curr=head
        while curr:
            copy=Node(curr.val)
            mapper[curr]=copy
            curr=curr.next
        curr=head
        while curr:
            copy=mapper[curr]
            copy.next=mapper[curr.next]
            copy.random=mapper[curr.random]
            curr=curr.next
        return mapper[head]
        