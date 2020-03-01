# 给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。 
# 
#  示例: 
# 
#  输入:
# [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# 输出: 6 
#  Related Topics 栈 数组 哈希表 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        res = 0
        dp = [0] * n
        for i in range(m):
            for j in range(n):
                dp[j] = 0 if matrix[i][j] == '0' else dp[j] + 1
            res = max(self.maxReactangle(dp), res)
        return res

    def maxReactangle(self, heights):
        stack = [-1]
        heights.append(0)
        n = len(heights)
        res = 0
        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                res = max(h * w, res)
            stack.append(i)
        heights.pop()
        return res

# leetcode submit region end(Prohibit modification and deletion)


print(Solution().maximalRectangle(
    [["1", "0", "1", "0", "0"],
     ["1", "0", "1", "1", "1"],
     ["1", "1", "1", "1", "1"],
     ["1", "0", "0", "1", "0"]]))
