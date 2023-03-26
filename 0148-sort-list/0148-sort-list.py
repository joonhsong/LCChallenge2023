# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        tmp = []
        cur = head
        curr = head
        while(cur):
            tmp.append(cur.val)
            cur = cur.next
        tmp.sort()
        for i in range(len(tmp)):
            curr.val = tmp[i]
            curr = curr.next
        return head