class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # hashmap : to store i,n
        # compliment
        #check to see if compliment inside map
        # if true, return indices

        # if not, add current i,n to map and move to next i


        tracker = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in tracker:
                return [tracker[diff], i]

            tracker[n] = i
        