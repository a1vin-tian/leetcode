# leetcode submit region begin(Prohibit modification and deletion)
import random
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(low, high):
            pivot = random.randint(low, high)
            nums[pivot], nums[high] = nums[high], nums[pivot]
            i = low
            for j in range(low, high):
                if nums[j] < nums[high]:
                    nums[j], nums[i] = nums[i], nums[j]
                    i += 1

            nums[i], nums[high] = nums[high], nums[i]
            return i

        def qs(low, high):
            if low < high:
                mid = partition(low, high)
                qs(low, mid - 1)
                qs(mid + 1, high)

        qs(0, len(nums) - 1)
        return nums


# leetcode submit region end(Prohibit modification and deletion)

print(Solution().sortArray([4, 8, 0, 2, 7]))
