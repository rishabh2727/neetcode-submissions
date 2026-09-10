# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            return TreeNode(val)

        cur = root
        while cur:
            if val > cur.val:
                # go right
                if not cur.right:
                    cur.right = TreeNode(val)
                    return root
                cur = cur.right
            else:
                if not cur.left:
                    cur.left = TreeNode(val)
                    return root
                cur = cur.left





      
    
# node = 5, val = 6
# parent = 5, 
# use stack
# stack = [(5, parent)]
# stack = [9,5]
# pop, val=6 is less than 9, and it is bigger than parent, so assign node.left = val, return


# val = 2
# stack = [5,inf]
# if val > node.val: go right, else go left
# if val < node.val, and larger than parent, assign accordingly.
# save 5 as 3's parent
# stack = [(3,5)]
# pop, val=2, val < 3 and less than 5,go left
# stack = [(1,3)]
# pop, val>node.val, but shorter than node.parent, so assign node.right = Node(2)







        