
class Solution:
    def isValid(self, s) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in pairs.values():
                stack.append(char)
            elif char in pairs.keys():
                if not stack or stack.pop() != pairs[char]:
                    return False
        
        return len(stack) == 0
