from typing import List

class Solution:

    def continious(self, numbers: List[int]) -> int:

        if not numbers:
            return 0

        count = 1
        longest = 1

        for pos in range(1, len(numbers)):

            if numbers[pos] == numbers[pos-1]:
                continue

            if numbers[pos-1] + 1 == numbers[pos]:
                count += 1
            else:
                count = 1

            longest = max(longest, count)

        return longest

    def longestConsecutive(self, nums: List[int]) -> int:

        return self.continious(sorted(nums))