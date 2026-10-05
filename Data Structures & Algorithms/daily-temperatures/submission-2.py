class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0]*len(temperatures)
        stack = []
        for i,j in enumerate(temperatures):

            while stack and j - stack[-1][1] > 0:
                diff = i - stack[-1][0]
                pos = stack[-1][0]
                output[pos] = diff
                stack.pop()
            stack.append([i , j])
        return output


