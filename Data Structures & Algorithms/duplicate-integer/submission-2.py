class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seenValues = set()

        for i in nums:
            if i in seenValues:
                return True

            seenValues.add(i)

        return False