class Solution:
    def isValid(self, s: str) -> bool:
        parentheses: dict[str, str] = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack: list[str] = []
        for ch in s:
            if ch in parentheses.values():
                stack.append(ch)
            else:
                if not stack or stack[-1] != parentheses[ch]:
                    return False
                else:
                    stack.pop()
        return True if not stack else False
