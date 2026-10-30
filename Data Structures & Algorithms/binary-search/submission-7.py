class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        first = 0
        last = len(nums) - 1
        while first <= last:
            midle = (last + first) // 2
            if nums[midle] == target:
                return midle
                
            elif nums[midle] > target:
                last = midle - 1
            else:
                first = midle + 1
        
        
        return -1
        