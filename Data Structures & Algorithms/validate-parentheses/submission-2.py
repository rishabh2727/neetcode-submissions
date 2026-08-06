class Solution:
    def isValid(self, s: str) -> bool:
        # "([{}])"

        stack = []
        my_dict = {"(": ")", "{": "}", "[": "]"}

        for bracket in s:
            if bracket in "({[":
                stack.append(bracket)
            else:
                if not stack:
                    return False
                opening_bracket = stack[-1]
                if my_dict[opening_bracket] == bracket:
                    stack.pop()
                else:
                    return False
        
        return not stack


                
                
                    





        
        
        
        