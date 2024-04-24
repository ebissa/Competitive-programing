# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy=ListNode(None)
        prev=dummy
        values=[]
        for i in range(len(lists)):
            node=lists[i]
            while node:
                values.append(node.val)
                prev.next=node
                prev=node
                node=node.next
        values.sort()
        current=dummy.next
        for num in values:
            current.val=num
            current=current.next
        return dummy.next
        
                
            
            
            
                
        
            
        