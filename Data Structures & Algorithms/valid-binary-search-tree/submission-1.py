# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # for every tree check if its left child is smaller and right
        # is bigger, use bounds, this is top down approach, we know 
        # the conditions from thw root itself, which can be checked while
        # we iterate from root to child, so the check comes before the 
        # recursive call.
        def dfs(node,lower, upper):
            if not node:
                return True
            if node.val <= lower or node.val >= upper:
                return False
            left = dfs(node.left,lower,node.val)
            right = dfs(node.right,node.val,upper)
            
            return left and right

        return dfs(root,float("-inf"),float("inf"))

    
# base condition would return False, as soon as we come across a 
# node whose value is not within the bounds, 
# if the node does not exist, continue and return True

# dfs(2,+inf, -inf)
# check if 2 not within the bounds, return False
# dfs(1,bounds are updated:-inf,2) 
# check if 1 is within the bounds, if not return False
# dfs(2) 
#     dfs(1)
#         dfs(None) -> return True
#         dfs(None) -> return True
#         return True
#     dfs(3)



    #     5
    #    / \
    #   1   4
    #      / \
    #     3   6




        