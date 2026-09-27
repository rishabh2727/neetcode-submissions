# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # its the leaf node
        # process children before the parents. process both of them
        # before the parents, so it will be postorder traversal
        if not root:
            return None
        
        root.left = self.removeLeafNodes(root.left,target)
        root.right = self.removeLeafNodes(root.right,target)

        if not root.left and not root.right and root.val == target:
            return None
        
        return root
# dfs(1)
#     dfs(2)
#         dfs(2)
#             dfs(None) -> None
#             dfs(None) -> None
#         left = None, right = None, value == target, 
#         so return None
#         dfs(None) -> None
#     left = None, right = None, value == target,
#     so return None
#     dfs(3)
#         dfs(2)
#             dfs(None)
#             dfs(None)
#             return None
#         dfs(4)
#             None
#             None
#         return 4
#     left = None, right = 4
#     return root = 3 as it is 
# left = None, right = 3
# return root
#     tree looks like, 
    #     1
    #    / \
    # None  3
    #        \ 
    #         4
