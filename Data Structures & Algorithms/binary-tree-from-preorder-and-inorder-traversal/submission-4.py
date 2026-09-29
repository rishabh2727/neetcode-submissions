# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {}
        for i, val in enumerate(inorder):
            inorder_map[val] = i
        counter = 0

        def dfs(l, r):
            nonlocal counter
            if l > r:
                return None

            root_val = preorder[counter]
            counter += 1
            root = TreeNode(root_val)
            mid = inorder_map[root_val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root

        return dfs(0, len(inorder) - 1)




# Input: preorder = [1,2,3,4], inorder = [2,1,3,4]
#         now we know the root which is 1
#         index is also 1
#         so how to build the tree?
#         2 will be on the left, 3,4 will be on the right,

#         preorder tells us more about the structure.

# the left subtree has x nodes, so grab the x elements right after the root in preorder. mid is important here, it tells us exactly how many elements
# left subtree has
        