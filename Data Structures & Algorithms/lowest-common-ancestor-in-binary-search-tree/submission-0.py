# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if p > node value, and q < node value,
        # then this node is the LCA
        # if both are greater than node val, check right subtree
        # find the point where they one is greater, the other is smaller
        # or vice versa
        # this is also top down approach, we can check the conditions
        # on the root itself.
        # this determines the split point
        if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
            return root
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return self.lowestCommonAncestor(root.left,p,q)




# dfs(5)
#     # 3,4 both smaller, so call left subtree
#     dfs(3), this is the split point -> returns 3



        