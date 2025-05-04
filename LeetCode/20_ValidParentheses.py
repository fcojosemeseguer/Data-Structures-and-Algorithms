class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in pairs.values():
                stack.append(char)
            elif char in pairs.keys():
                if not stack or stack.pop() != pairs[char]:
                    return False

        return not stack
