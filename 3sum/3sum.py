class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        r = set()
        nums.sort()
        for i, a in enumerate(nums[:-2]):
            m = {}
            for b in nums[i + 1:]:
                if b not in m:
                    m[-a - b] = 1
                else:
                    r.add((a, -a - b, b))
        return map(list, r)


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
