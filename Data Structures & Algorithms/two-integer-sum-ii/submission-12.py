class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(numbers)):
            searched = target - numbers[i]
            if seen.get(searched) is not None:
                return [seen[searched], i + 1]
            else:
                seen[numbers[i]] = i + 1
                
