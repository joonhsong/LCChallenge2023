# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        trav = []
        def traverse(root, trav):
            if root == None:
                return
            traverse(root.left, trav)
            trav.append(root.val)
            traverse(root.right, trav)
        traverse(root, trav)
        for i in range(1, len(trav)):
            if trav[i] <= trav[i-1]:
                return False
        return True
        
            