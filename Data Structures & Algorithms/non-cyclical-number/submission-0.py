class Solution:
    def isHappy(self, n: int) -> bool:
        seen_nums = set()

        result = n        
        while result != 1:            
            digits = str(result)
            result = 0
            for digit in digits:
                result += int(digit) ** 2
            
            if result in seen_nums:
                return False
            else:
                seen_nums.add(result)
                
        return True
        