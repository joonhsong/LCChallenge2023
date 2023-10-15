# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.dfs(root)
        return self.diameter
    def dfs(self, root):
        if not root:
            return 0
        left_h = self.dfs(root.left)
        right_h = self.dfs(root.right)
        self.diameter = max(self.diameter,left_h + right_h)
        return max(left_h,right_h) + 1
        

    