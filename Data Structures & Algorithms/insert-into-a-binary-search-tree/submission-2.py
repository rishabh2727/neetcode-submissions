# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # this base case is where we find the position in the tree where the node
        # has to be inserted.
        if not root:
            return TreeNode(val)

        if val > root.val:
            node = self.insertIntoBST(root.right,val)
            root.right = node        
        else:
            node = self.insertIntoBST(root.left,val)
            root.left = node

        return root
        


# insert(5)
# insert(9), 9.right = 6
# insert(None) -> Node(6)