# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        mlist = []
        head = ListNode(0)
        tmp = head
        
        for i in lists:
            while i != None:
                mlist.append(i.val)
                i = i.next
        
        mlist.sort()
        
        for j in mlist:
            tmp.next = ListNode(j)
            tmp = tmp.next
        return head.next
            
        

                