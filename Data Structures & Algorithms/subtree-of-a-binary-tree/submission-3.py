# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # try all three solutions, stack, recursion, and BFS
        # if root's value is equal to the subtree's value
        # start building the stack, and checking
        def sameTree(p,q):
            stack = [(p,q)]
            while stack:
                node_p, node_q = stack.pop()
                if not node_p and not node_q:
                    continue
                if not node_p or not node_q or node_p.val != node_q.val :
                    return False
                
                stack.append((node_p.left, node_q.left))
                stack.append((node_p.right, node_q.right))
            
            return True

# root=[1,1]
# subRoot=[1]
            
        s = [(root, subRoot)]
        while s:
            node1, node2 = s.pop()
            if node1.val == node2.val:
                print("Ran Function")
                if sameTree(node1, node2):
                    return True
            if node1.left:
                    s.append((node1.left, node2))
            if node1.right:
                    s.append((node1.right, node2))
            
        return False
        


            
            # now check if values and structure are same


                
            



        # while root and subRoot
        # stack = [(2,2)]
        # stack = [(4,4)]



        # [1,2,3,None,None,]



        
        