class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            final = target - num

            if final in seen:
                return [seen[final], i]
            seen[num] = i