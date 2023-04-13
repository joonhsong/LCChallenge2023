# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        linlis = []
        for i in lists:
            while i != None:
                linlis.append(i.val)
                i = i.next
        linlis.sort()
        head = ListNode(0)
        temp = head
        for j in linlis:
            temp.next = ListNode(j)
            temp = temp.next
        return head.next