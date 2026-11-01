class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        for num in nums:
            if seen.get(num) is None:
                seen[num] = 1
            else:
                seen[num] += 1

        return [tup[0] for tup in list(sorted(seen.items(), key = lambda item: item[1]))[-k:] ]
        
        