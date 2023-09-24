# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head
        palin = []
        while temp is not None:
            palin.append(temp.val)
            temp = temp.next
        
        def checkpalindrome(p):
            start = 0
            end = len(p) - 1
            
            while start <= end:
                if p[start] != p[end]:
                    return False
                start += 1
                end -= 1
            return True
        
        return checkpalindrome(palin)
        
            
        