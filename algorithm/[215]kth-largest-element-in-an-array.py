# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。 
# 
#  请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
#  
# 
#  示例 2: 
# 
#  
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= k <= nums.length <= 104 
#  -104 <= nums[i] <= 104 
#  
#  Related Topics 数组 分治 快速选择 排序 堆（优先队列） 
#  👍 1230 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def partition(left, right):
            p = random.randint(left, right)
            nums[p], nums[right] = nums[right], nums[p]
            i = left
            for j in range(left, right):
                if nums[j] < nums[right]:
                    nums[j], nums[i] = nums[i], nums[j]
                    i += 1
            nums[i], nums[right] = nums[right], nums[i]
            return i

        def qs(left, right, index):
            p = partition(left, right)
            if p == index:
                return nums[index]
            elif p < index:
                return qs(p + 1, right, index)
            else:
                return qs(left, p - 1, index)

        return qs(0, len(nums) - 1, len(nums) - k)


# leetcode submit region end(Prohibit modification and deletion)

print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2))
