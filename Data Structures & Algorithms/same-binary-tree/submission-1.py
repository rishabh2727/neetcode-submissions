# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # using bfs to do it. explore level by level
        # compare each node in the same order.
        # take two queues.
        q1 = deque()
        q2 = deque()

        q1.append(p)
        q2.append(q)
        while q1 or q2:

            node1 = q1.popleft()
            node2 = q2.popleft()
            if not node1 and not node2:
                continue
            if not node1 and node2 or not node2 and node1:
                return False
            if node1.val != node2.val:
                return False
            # add children
            q1.append(node1.left)
            q2.append(node2.left)
            q1.append(node1.right)
            q2.append(node2.right)
        
        return True

            





            







        #     if not p and not q:
        #         return True
        #     if not p and q or p and not q:
        #         return False
        #     if p.val != q.val:
        #         return False

        #     left = dfs(p.left,q.left)
        #     right = dfs(p.right,q.right)

        #     return left and right
        
        # return dfs(p,q)
    # the maximum stack size at any moment = the length of the longest path from root
    #  to leaf = height of the tree.

    # The space is used by the call stack. Each recursive call to
    #  dfs sits on the stack until it returns. The deepest 
    # the stack ever gets equals the height h of the tree.
# For a balanced tree — h = log(n), so space is O(log n)
# For a skewed tree (like a linked list) — h = n, so space is O(n)
# Every node in both trees is visited exactly once. 
# At each node you do constant work — 3 if checks and 
# that's it. So if the trees have n nodes total, it's O(n).
# Worst case is when both trees are identical — you visit every single 
# node before confirming they match. 

        