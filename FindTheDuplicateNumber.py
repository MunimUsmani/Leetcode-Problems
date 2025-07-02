class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        store_unique = set()
        for item in nums:

            if item in store_unique:

                return item

            store_unique.add(item)
