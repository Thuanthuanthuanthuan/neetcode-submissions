class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_count = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in num_count:
                return [num_count[diff], i]

            num_count[n] = i
        