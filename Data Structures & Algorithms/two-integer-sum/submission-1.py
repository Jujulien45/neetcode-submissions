class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums) - 1):
            for y in range(i + 1, len(nums)):
                if nums[i] + nums[y] == target:
                    if i < y:
                        return [i, y]
                    else:
                        return [y, i]
        