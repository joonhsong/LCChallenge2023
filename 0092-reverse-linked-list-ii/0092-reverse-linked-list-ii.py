# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        temp = head
        rev = []
        while temp is not None:
            rev.append(temp.val)
            temp = temp.next
        rev[left-1:right] = reversed(rev[left-1:right])
        store = head
        for i in range(len(rev)):
            head.val = rev[i]
            head = head.next
        head = store
        
        return head
        