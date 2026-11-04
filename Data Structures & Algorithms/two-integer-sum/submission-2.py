class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for i in range(len(nums)):
            searched = target - nums[i]
            if searched in seen:
                if i < seen[searched]:
                    return [i, seen[searched]]
                else:
                    return [seen[searched], i]
            
            seen[nums[i]] = i
        