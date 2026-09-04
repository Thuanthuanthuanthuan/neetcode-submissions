class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_seen = {}

        for i, n in enumerate(nums):
            complement = target - n
            if complement in num_seen:
                return [num_seen[complement], i]

            num_seen[n] = i
        