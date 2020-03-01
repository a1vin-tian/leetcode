# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。 
# 
#  示例 1: 
# 
#  输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
#  
# 
#  示例 2: 
# 
#  输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
#  
#  Related Topics 字符串 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        use stack
        :param s:
        :return:
        """

        if not s: return 0
        n = len(s)
        res = 0
        stack = [-1]
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(i - stack[-1], res)
        return res

    def longestValidParenthesesDP(self, s: str) -> int:
        """
        dp[i] = s[i]结尾的最长有效括号数
        dp[i] = {
            如果前一个是 (
            dp[i-2] + 2
            如果前一个是 ) 并且 有对应的有效匹配括号
            dp[i] = dp[i - 1] + (dp[i - 2] if i - dp[i - 1] >= 2 else 0) + 2
        }
        :param s:
        :return:
        """
        if not s: return 0
        n = len(s)

        dp = [0] * n
        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2 if i >= 2 else 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + (dp[i - 2] if i - dp[i - 1] >= 2 else 0) + 2
        return max(dp)


# leetcode submit region end(Prohibit modification and deletion)

print(Solution().longestValidParentheses("()((()))"))
