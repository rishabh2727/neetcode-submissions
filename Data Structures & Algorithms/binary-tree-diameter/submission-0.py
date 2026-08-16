# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
# For any node, the longest path through that node = (height of its left side) + (height of its right side).
# dfs(1)
# left = dfs(None) -> 0
# right = dfs(2) -> 4

# dfs(2) -> 1 + 2 + 1 -> 4
# left = dfs(3) -> 2
# right = dfs(4) -> 1

# dfs(3)
# left = dfs(5) -> 1
# right = dfs(none) -> 0

# dfs(5) -> 1
        res = 0
        def helper(root):
            nonlocal res
            if not root:
                return 0
            
            left = helper(root.left)
            right = helper(root.right)

            res = max(res, left+right)

            return max(left, right) + 1
        
        helper(root)
        return res
        
    
    




            



        