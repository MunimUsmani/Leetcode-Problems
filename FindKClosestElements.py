class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k  # Only search till len - k

        while l < r:
            m = (l + r) // 2
            # Compare distances: x - arr[m] vs arr[m + k] - x
            if x - arr[m] > arr[m + k] - x:
                l = m + 1
            else:
                r = m

        return arr[l:l + k]  # Return the closest k elements
