class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        num_tracker = {}

        for i, n in enumerate(numbers):
            diff = target - n

            if diff in num_tracker:
                return [num_tracker[diff] + 1, i + 1]

            num_tracker[n] = i

        