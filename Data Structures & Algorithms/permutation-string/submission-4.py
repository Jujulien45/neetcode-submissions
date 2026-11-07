class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        for char in s1:
                
            if char not in s2:
                return False
        

        for i in range(len(s2) - len(s1) + 1):
            sub_s = s2[i:i + len(s1)]
            print(sub_s)
            
            if sorted(sub_s) == sorted(s1):
                return True
        
        return False