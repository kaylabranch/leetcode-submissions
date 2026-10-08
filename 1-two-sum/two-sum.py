class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_map = {}

        for i, num in enumerate(nums):
            remainder = target - num

            if remainder in nums_map:
                return [nums_map[remainder], i]
            
            nums_map[num] = i