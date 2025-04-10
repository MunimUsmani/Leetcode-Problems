class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {"(": ")", "{": "}", "[": "]"}

        for parenthese in s:
            if parenthese in lookup:
                stack.append(parenthese)
            elif not stack or lookup[stack.pop()] != parenthese: 
                return False

        return len(stack) == 0
