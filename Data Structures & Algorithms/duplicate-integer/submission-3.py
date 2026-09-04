class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        duplicateMap = set()

        for num in nums:
            if num in duplicateMap:
                return True

            duplicateMap.add(num)
        return False


        