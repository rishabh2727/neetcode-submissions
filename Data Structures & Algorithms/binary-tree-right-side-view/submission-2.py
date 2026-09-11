from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # iterate, go level by level, use a queue.
        
        queue = deque([root])
        if not root:
            return []
        res = []

        while queue:
            cur_length = len(queue)
            for i in range(cur_length):
                node = queue.popleft()  
                if i == cur_length-1:
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return res



# queue = [1]
# length = 1, i == cur_length-1, so add to res
# pop 1 from queue, 
# queue = [2,3], cur_legnth = 2, i = 0
# queue = [3,4], cur_length = 2, i = 1 == cur_legnth-1
# pop 3, res = [1,3]
# queue = [4,5], 
# length calculated again, cur_length = 2
# # check if this is the last element, that is the element at the right end of a level
# queue = [2,3]
# how to know it is the loop's last iteration,
# save in a variable, the length of queue at that time, and then check if current iteration
# i is equal to that length-1, 







        





        
        