class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, y = len(numbers) - 2, len(numbers) - 1
        while numbers[i] + numbers[y] != target:
            if numbers[i] + numbers[y] < target:
                y += 1
            else:
                i -= 1
                y -= 1
        
        return [i + 1, y + 1]
