# 找出数组中重复的数字。 
# 
#  
# 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请
# 找出数组中任意一个重复的数字。 
# 
#  示例 1： 
# 
#  输入：
# [2, 3, 1, 0, 2, 5, 3]
# 输出：2 或 3 
#  
# 
#  
# 
#  限制： 
# 
#  2 <= n <= 100000 
#  Related Topics 数组 哈希表 排序 👍 521 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            if nums[i] == nums[nums[i]]: return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return - 1

    def findRepeatNumberHash(self, nums: List[int]) -> int:
        m = set()
        for n in nums:
            if n in m:
                return n
            m.add(n)
        return


# leetcode submit region end(Prohibit modification and deletion)

print(Solution().findRepeatNumber([2, 3, 1, 0, 2, 5, 3]))
