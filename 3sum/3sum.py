class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        r = set()
        nums.sort()
        for i in xrange(len(nums)):
            for k in xrange(i + 1, len(nums)):
                for j in xrange(k + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        r.add((nums[i], nums[j], nums[k]))

        return list([list(n) for n in r])


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
