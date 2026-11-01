class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)

        for num in nums:
            seen[num] += 1

        return [tup[0] for tup in list(sorted(seen.items(), key = lambda item: item[1]))[-k:] ]
        
        