# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # depth first search with left branch first, root and then right
        lst = []
        def helper(node):
            nonlocal lst
            if not node:
                return None
            helper(node.left)
            lst.append(node.val)
            helper(node.right)
            

        helper(root)
        return lst





array = [4,]
        

        