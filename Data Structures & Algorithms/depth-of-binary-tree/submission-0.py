# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left,right)






























        # if not root:
        #     return 0
        # left = self.maxDepth(root.left)
        # right = self.maxDepth(root.right)
        # return max(left,right) + 1
        if not root:
            return 0
        
        depth = 0
        q = deque()
        q.append(root)
        # we have to process each level.
        while q: 
            for i in range(len(q)):
                node = q.popleft()
            # if the node has children, we add them to the queue.
            # we process all the nodes at the same level.
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth += 1
        return depth

# Time Complexity — O(n)
# Every single node is visited exactly once. 
# No node is added to the queue twice, no node is processed twice.
# The space is used by the queue q. The question is: how many nodes
#  can be in the queue at once?
# The queue holds one level at a time. The worst case is the widest level
#  of the tree.
# For a perfect binary tree (every level completely full), 
# the bottom level has roughly n/2 nodes. So the queue could 
# hold n/2 nodes at once, which is still O(n).


        