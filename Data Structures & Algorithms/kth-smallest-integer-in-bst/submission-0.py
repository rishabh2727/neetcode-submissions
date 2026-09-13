# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # if you do an inorder traversal, then that will give us a
        # sorted array.
        res = []
        def dfs(node):
            
            if not node:
                return None
            
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)


        dfs(root)
        return res[k-1]

# root=[2,1,3]
# k=1

# dfs(2)
# dfs(1) -> 
# dfs(none) -> returns None
        

        


        