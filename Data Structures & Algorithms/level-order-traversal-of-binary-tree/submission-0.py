from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        lst = []
        while queue:
            temp = []
            for _ in range(len(queue)): 
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            lst.append(temp)
                
        
        return lst



# queue = [1], temp = [1], temp = [2,3]
# queue = [2,3]
# queue = 
# for loop equal to length of queue:
#     temp = []
#     temp.append(node)

# [1]
# [2,3]
# [3,4,5]
# [4,5,6,7]




        
        