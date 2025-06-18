import collections

class Solution:
    def maxDifference(self, s: str) -> int:
        counts = collections.Counter(s)
        max_odd = 0
        min_even = float('inf')
        found_even = False

        for freq in counts.values():
            if freq % 2 == 1:  # odd frequency
                max_odd = max(max_odd, freq)
            else:  # even frequency
                min_even = min(min_even, freq)
                found_even = True

        if not found_even:
            return max_odd  # can't subtract if no even frequency found

        return max_odd - min_even
