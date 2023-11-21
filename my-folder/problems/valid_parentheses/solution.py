class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closetoOpen = {")":"(","}":"{","]":"["}
        for bracket in s:
            if bracket in closetoOpen:
                if stack and stack[-1] == closetoOpen[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        return True if not stack else False