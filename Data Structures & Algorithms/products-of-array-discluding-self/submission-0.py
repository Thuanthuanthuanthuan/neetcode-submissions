class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        num_length = len(nums)
        res = [1] * num_length

        left_product = 1
        for i in range(num_length):
            res[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(num_length - 1, -1, -1):
            res[i] *= right_product
            right_product *= nums[i]
        return res
