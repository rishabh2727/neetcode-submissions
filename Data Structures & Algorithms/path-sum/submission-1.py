# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # try evry single path, which can be done using dfs.
        if not root:
            return False
# if a node has no left or right child, that means it is a leaf node.
        def dfs(node, cur_sum):
            if not node.left and not node.right:
                if cur_sum == targetSum:
                    return True
                else:
                    return False
            left, right = False,False
            if node.left:
                left = dfs(node.left, cur_sum+node.left.val)
            if node.right:
                right = dfs(node.right, cur_sum+node.right.val)

            return left or right
        
        return dfs(root, root.val)
        