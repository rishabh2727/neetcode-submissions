class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # stack = []
        # stack = [2]
        # stack = [2,4]
        # if element is negative:
        #     pop from stack
        # 4,-4
        # stack = [2]
        # pop again cause element is -1
        # stack = [2]

        stack = []
        for ast in asteroids:
            while stack and stack[-1] > 0 and ast < 0:
                element = stack.pop()
                element_val = abs(element)
                ast_val = abs(ast)
                if element_val < ast_val:
                    continue
                elif element_val > ast_val:
                    stack.append(element)
                    break
                else:
                    break
            else:
                stack.append(ast)
        return stack

        