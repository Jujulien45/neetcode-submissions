class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_chars = {}
        
        for char in s1:
                
            if char not in s2:
                return False

            s1_chars[char] = 1 + s1_chars.get(char, 0)
        
        sub_chars = {}
        for i in range(len(s1)):
            sub_chars[s2[i]] = 1 + sub_chars.get(s2[i], 0)
        if sub_chars == s1_chars:
            return True
        
        for i in range(len(s2) - len(s1)):
            y = i + len(s1)
            sub_chars[s2[y]] = 1 + sub_chars.get(s2[y], 0)
            if sub_chars.get(s2[i]) == 1:
                del sub_chars[s2[i]]
            else:
                sub_chars[s2[i]] -= 1
            if sub_chars == s1_chars:
                return True
        
        return False