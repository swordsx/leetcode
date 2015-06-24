class Solution:
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, height):
        height.append(0)
        stack = []
        result = 0
        for i in range(len(height)):
            if not stack or height[i] > height[stack[-1]]:
                stack.append(i)
            else:
                while stack and height[stack[-1]] > height[i]:
                    j = stack.pop()
                    result = max(result, height[j] * ((i - stack[-1] - 1) if stack else i))
                stack.append(i)
        return result
