class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        num_seen = {}

        for i, n in enumerate(numbers):
            diff = target - n
            if diff in num_seen:
                return [num_seen[diff] + 1, i + 1]

            num_seen[n] = i
        