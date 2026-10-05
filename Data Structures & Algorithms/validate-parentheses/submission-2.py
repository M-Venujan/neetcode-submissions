class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeopen = {")" : "(" , "]" : "[" , "}" : "{"}
        for i in s:
            if i in closeopen:
                if stack and stack[-1] == closeopen[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False

            

