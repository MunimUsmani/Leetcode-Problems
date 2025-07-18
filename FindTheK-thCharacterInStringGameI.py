class Solution:
    def kthCharacter(self, k: int) -> str:
        ones = (k - 1).bit_count()        
        return chr(ord('a') + ones)   
