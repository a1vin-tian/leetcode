# 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "We are happy."
# 输出："We%20are%20happy." 
# 
#  
# 
#  限制： 
# 
#  0 <= s 的长度 <= 10000 
#  Related Topics 字符串 👍 150 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def replaceSpace(self, s: str) -> str:
        sl = [''] * (len(s) * 3)
        size = 0
        for c in s:
            if c == ' ':
                sl[size] = '%'
                size += 1
                sl[size] = '2'
                size += 1
                sl[size] = '0'
                size += 1
            else:
                sl[size] = c
                size += 1
        return "".join(sl)


# leetcode submit region end(Prohibit modification and deletion)

print(Solution().replaceSpace("We are happy."))
