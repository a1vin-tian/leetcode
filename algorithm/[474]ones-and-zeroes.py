# 在计算机界中，我们总是追求用有限的资源获取最大的收益。 
# 
#  现在，假设你分别支配着 m 个 0 和 n 个 1。另外，还有一个仅包含 0 和 1 字符串的数组。 
# 
#  你的任务是使用给定的 m 个 0 和 n 个 1 ，找到能拼出存在于数组中的字符串的最大数量。每个 0 和 1 至多被使用一次。 
# 
#  注意: 
# 
#  
#  给定 0 和 1 的数量都不会超过 100。 
#  给定字符串数组的长度不会超过 600。 
#  
# 
#  示例 1: 
# 
#  
# 输入: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
# 输出: 4
# 
# 解释: 总共 4 个字符串可以通过 5 个 0 和 3 个 1 拼出，即 "10","0001","1","0" 。
#  
# 
#  示例 2: 
# 
#  
# 输入: Array = {"10", "0", "1"}, m = 1, n = 1
# 输出: 2
# 
# 解释: 你可以拼出 "10"，但之后就没有剩余数字了。更好的选择是拼出 "0" 和 "1" 。
#  
#  Related Topics 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
import collections
from typing import List


class Solution1:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """
        dp[k][i][j] = strs[0..k] 能够使用i个0和j个1组成的最大数值

        dp[k][i][j] = {
            dp[i+1]
        }

        :param strs:
        :param m:
        :param n:
        :return:
        """
        mem = {}

        def dp(i, m, n):
            if (i, m, n) not in mem:
                if i == len(strs):
                    ans = 0
                else:
                    counter = collections.Counter(strs[i])
                    zero = counter['0']
                    one = counter['1']
                    if m >= zero and n >= one:
                        ans = max(dp(i + 1, m - zero, n - one) + 1, dp(i + 1, m, n))
                    else:
                        ans = dp(i + 1, m, n)
                mem[(i, m, n)] = ans
            return mem[(i, m, n)]

        return dp(0, m, n)


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """
        dp[k][i][j] = strs[0..k] 能够使用i个0和j个1 组成的最大数值

        dp[k][i][j] = {
             max(dp(i - 1, m - zero, n - one) + 1, dp(i - 1, m, n)) , if m >= zero and n >= one:
            dp(i - 1, m, n),
        }

        :param strs:
        :param m:
        :param n:
        :return:
        """
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            counter = collections.Counter(s)
            zero = counter['0']
            one = counter['1']
            for i in range(m, zero - 1, -1):
                for j in range(n, one - 1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i - zero][j - one])
        return dp[-1][-1]


# leetcode submit region end(Prohibit modification and deletion)

print(Solution().findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3) == 4)
print(Solution().findMaxForm(["10", "0", "1"], 1, 1) == 2)
print(Solution().findMaxForm(["0", "0", "1", "1"], 2, 2) == 4)
