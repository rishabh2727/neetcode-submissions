import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack = [
        #     -
        #     4
        #     9
        # ]
        # curr = 1+2 = 3
        # append 3 to stack
        # curr = 3*3 = 9
        # append 3 to stack
        # 9-4 = 5
        # return stack.pop()
        # how to get elements out of stack 
        # in a way I can perform operators


# Map the string characters to their actual math functions
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.floordiv  # Use operator.floordiv for // integer division
        }

        stack = []
        for c in tokens:
            if c in "+-*/" and stack:
                operation = ops[c]
                second = stack.pop()
                first = stack.pop()
                if c == "/":
                    res = int(first/second)
                else:
                    res = operation(first,second)
                stack.append(res)
            else:
                stack.append(int(c))

        print(stack)
        return stack.pop()
        



        