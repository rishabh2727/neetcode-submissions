# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            if left == -1:
                return -1

            right = dfs(node.right)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1
            return max(left,right) + 1
        if dfs(root) == -1:
            return False
        else:
            return True



# dfs(1)
#     dfs(2)
#         dfs(None) -> 0
#         dfs(None) -> 0
#         check if difference between left and right is not more than 1
#         if abs(left - right) > 1:
#             return -1
#         return max(0,0)+1 -> 1

#     dfs(3)
#         dfs(4)
#             dfs(None) -> 0
#             dfs(None) -> 0
#             return max(left,right) + 1 -> 1
#         dfs(None) -> 0
#         left = 1, right = 0
#         if abs(left-right) > 1: return -1,
#         return max(left,right) + 1
#         return 2 here
    
#     left = 1
#     right = 2
#     if abs(left-right) > 1: return -1,
#     return max(left,right) + 1
#     we return 3

#     if dfs(root) != -1





        
        
        