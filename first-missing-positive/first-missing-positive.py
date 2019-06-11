# class Solution(object):
#     def firstMissingPositive(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         m = set()
#         max = 0
#         for n in nums:
#             m.add(n)
#             if n > max:
#                 max = n
#         for n in xrange(1, max):
#             if n not in m:
#                 return n
#         return max + 1

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            while 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                t = nums[i]
                nums[i] = nums[nums[i] - 1]
                nums[t - 1] = t
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1


if __name__ == '__main__':
    Solution().firstMissingPositive([3, 4, -1, 1])
