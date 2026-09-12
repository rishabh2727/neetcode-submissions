# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0
        def dfs(node,max_val):
            nonlocal good_nodes
            if not node:
                return

            if node.val >= max_val:
                max_val = node.val
                good_nodes += 1
            
            dfs(node.left,max_val)
            dfs(node.right, max_val)

            return
    
        dfs(root, root.val)
        return good_nodes




# dfs(2, max_val=2) -> good_node += 1
# dfs(1,2)
# dfs(1,2)
# dfs(5,5) -> good_node += 1
# dfs(1,2) -> return
# dfs(3,2) -> good_node += 1, 

