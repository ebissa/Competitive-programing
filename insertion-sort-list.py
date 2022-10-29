class Solution(object):
    def insertionSortList(self, head):
        dummy=ListNode(0,head)
        prev,cur=head,head.next
        while cur:
            if cur.val>=prev.val:
                prev,cur=cur,cur.next
                continue
            temp=dummy
            while cur.val>temp.next.val:
                temp=temp.next
            prev.next=cur.next
            cur.next=temp.next
            temp.next=cur
            cur=prev.next
        return dummy.next