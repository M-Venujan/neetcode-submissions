class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        signs = ['+' , '-' , '*' , '/']
        stack = []
        res = 0
        for i in tokens:
            if i not in signs:
                stack.append(int(i))
            else:
                a = stack[-1]
                stack.pop()
                b = stack[-1]
                stack.pop()
                if i == '+':
                    stack.append(b + a)
                elif i == '-':
                    stack.append(b - a)
                elif i == '*':
                    stack.append(b * a)
                elif i == '/':
                    stack.append(int(b / a))
        return stack[-1]
                