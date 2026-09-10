from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        queue = deque()
        queue.append(root)
        direction = 1

        while queue:
            temp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if direction % 2 == 0:
                res.append(temp[::-1])
            else:
                res.append(temp)
            direction += 1

        return res


# queue = [1]
# pop 1 node out, add children
# queue = [6,7,4,5]
# pop 3, add children
# queue = [3,4,5]
# pop 3, add children
# queue = [4,5,6,7]

# make sure the entire level is processed and their children have been added,
# since they have to be added in a specific order.
# for processing all nodes and adding their children at one level, I have to use
# a for loop.
# direction variable, switch it after for loop finishes

        