class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        new_nums = set(nums)
        longest = 0

        for n in new_nums:
            #check if n is start of sequence
            if (n-1) not in new_nums:
                length = 1

                while (n + length) in new_nums:
                    length += 1

                longest = max(length, longest)

        return longest


        
        