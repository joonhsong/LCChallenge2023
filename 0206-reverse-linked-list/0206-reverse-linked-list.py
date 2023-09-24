# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        rev = []
        while temp != None:
            rev.append(temp.val)
            temp = temp.next
        rev.reverse()
        store = head
        for i in rev:
            head.val = i
            head = head.next
        head = store
        return head
            