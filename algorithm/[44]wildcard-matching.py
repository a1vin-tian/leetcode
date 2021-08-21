# 给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。 
# 
#  '?' 可以匹配任何单个字符。
# '*' 可以匹配任意字符串（包括空字符串）。
#  
# 
#  两个字符串完全匹配才算匹配成功。 
# 
#  说明: 
# 
#  
#  s 可能为空，且只包含从 a-z 的小写字母。 
#  p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。 
#  
# 
#  示例 1: 
# 
#  输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。 
# 
#  示例 2: 
# 
#  输入:
# s = "aa"
# p = "*"
# 输出: true
# 解释: '*' 可以匹配任意字符串。
#  
# 
#  示例 3: 
# 
#  输入:
# s = "cb"
# p = "?a"
# 输出: false
# 解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
#  
# 
#  示例 4: 
# 
#  输入:
# s = "adceb"
# p = "*b*b"
# 输出: true
# 解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
#  
# 
#  示例 5: 
# 
#  输入:
# s = "acdcb"
# p = "a*c?b"
# 输入: false 
#  Related Topics 贪心算法 字符串 动态规划 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        mem = {}

        def dp(i, j):
            if (i, j) not in mem:
                if i == len(s) and j == len(p):
                    ans = True
                elif j == len(p):
                    ans = False
                elif i == len(s):
                    ans = p[j] == "*" and dp(i, j + 1)
                else:
                    if p[j] == "*":
                        ans = dp(i, j + 1) or dp(i + 1, j)
                    else:
                        ans = i < len(s) and p[j] in [s[i], '?'] and dp(i + 1, j + 1)
                mem[(i, j)] = ans
            return mem[(i, j)]

        return dp(0, 0)


class SolutionDP:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            dp[0][i] = dp[0][i - 1] and p[i - 1] == '*'
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] in {s[i - 1], '?'}:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        return bool(dp[-1][-1])


# leetcode submit region end(Prohibit modification and deletion)

print(Solution().isMatch("acdcb", "a*c?b") == False)
print(Solution().isMatch("aa", "a*") == True)
print(Solution().isMatch("aa", "a") == False)
print(Solution().isMatch("cb", "?a") == False)
print(Solution().isMatch("adceb", "*a*b") == True)
print(Solution().isMatch("a", "a*") == True)
print(Solution().isMatch("a", "a************") == True)
