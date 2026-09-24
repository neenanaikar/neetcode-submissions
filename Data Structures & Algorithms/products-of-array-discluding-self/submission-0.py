class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        left = 1
        for i in range(len(nums)):
            output[i] = left
            left *= nums[i] ## multiply current one after we store
        
        right = 1
        for i in range(len(nums)-1, -1, -1): ## moving from right to left
            output[i] *= right ## multiply everything in after i
            right *= nums[i] ## mult curr one after we store

        return output