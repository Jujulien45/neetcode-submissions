class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_chars = {}
        
        for char in s1:
                
            if char not in s2:
                return False

            if s1_chars.get(char) is None:
                s1_chars[char] = 1
            else:
                s1_chars[char] += 1
        

        for i in range(len(s2) - len(s1) + 1):
            sub_s = s2[i:i + len(s1)]
            print(sub_s)

            sub_chars = {}
            for char in sub_s:
                if sub_chars.get(char) is None:
                    sub_chars[char] = 1
                else:
                    sub_chars[char] += 1
            
            if sub_chars == s1_chars:
                return True
        
        return False