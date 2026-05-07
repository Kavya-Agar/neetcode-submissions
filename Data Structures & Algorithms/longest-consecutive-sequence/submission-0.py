class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for i in nums:
            if (i - 1) not in numSet:
                n = 0
                while (i + n) in numSet:
                    n += 1
                longest = max(n, longest)
        return longest