from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        # Sort values by frequency, highest first
        values = sorted(count, key=count.get, reverse=True)

        return values[:k]