class Solution:
    def simplifyPath(self, path: str) -> str:
        pth = path.split('/')
        stack = []
        
        for element in pth:
            if element == ".":
                continue
            elif element == "..":
                if stack:
                    stack.pop()
            elif element == "":
                if stack and stack[-1] == "/":
                    continue
            else:
                stack.append(element)
            print(stack)
        
        return "/" + "/".join(stack)

            
            

        

        









        