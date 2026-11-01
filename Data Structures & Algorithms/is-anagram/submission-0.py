class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_s = {}
        for char in s:
            if seen_s.get(char) is None:
                seen_s[char] = 1
            else:
                seen_s[char] += 1

        seen_t = {}
        for char in t:
            if seen_t.get(char) is None:
                seen_t[char] = 1
            else:
                seen_t[char] += 1

        return seen_t == seen_s