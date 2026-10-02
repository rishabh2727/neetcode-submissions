# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total_sum = 0
        def dfs(node):
            nonlocal total_sum
            if not node:
                return 0
            if low <= node.val <= high:
                total_sum += node.val

            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return total_sum


        
#         bottom down, keep checking the values, simple recursion.

# dfs(5)
#     dfs(3)
#         dfs(1)
#             dfs(none) -> 0
#             dfs(2)
#                 dfs(None) -> 0
#                 dfs(None) -> 0
            