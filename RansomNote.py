class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_map = {}

        for char in magazine:
            if char in magazine_map:
                magazine_map[char] += 1
            else:
                magazine_map[char] = 1

        for char in ransomNote:
            if char not in magazine_map or magazine_map[char] == 0:
                return False
            magazine_map[char] -= 1

        return True
