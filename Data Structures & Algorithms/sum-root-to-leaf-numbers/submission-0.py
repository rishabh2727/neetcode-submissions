# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        lst = []

# use a temp lst, once a leaf node is reached, all the numbers we
# saw in the path, path = "", add the numbers as a string in path
# path will look like "123", then add this path to a temp array as one
# single number. do same for all root to leaf paths.
        def dfs(node, path):
            path = path+str(node.val)
            if not node.left and not node.right:
                lst.append(int(path))
                return
            
            if node.left:
                dfs(node.left,path)
            if node.right:
                dfs(node.right,path)
            
            return 
        
        dfs(root,"")
        return sum(lst)


# dfs(1,"1") -> return
# dfs(5,"15") -> add to lst, return
# dfs(1,"11") -> return 
# dfs(6,"116") -> add to lst, return 

        