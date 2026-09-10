from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # left and right subtree get switched
        # go down the next level, and do the same thing.
        # maybe use a queue, and do a level ordee traversal.
        if not root:
            return root

        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if not node.left and not node.right:
                continue
            saveNode = node.left
            node.left = node.right
            node.right = saveNode

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root



        