# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def check(mirl, mirr):
            if mirl==None and mirr==None:
                return True
            if mirl==None or mirr==None:
                return False
            if mirl.val==mirr.val:
                if check(mirl.left, mirr.right) and check(mirl.right, mirr.left):
                    return True
            return False
        return check(root.left, root.right)
                    
                
            
        
        