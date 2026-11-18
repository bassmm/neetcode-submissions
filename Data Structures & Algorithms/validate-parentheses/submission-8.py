class Solution:
    def isValid(self, s: str) -> bool:

        matches = {
            "[":"]",
            "{":"}",
            "(":")"
        }
        if s[0] not in ("[", "(", "{"):
            return False
        
        stack = [s[0]]

        for c in s[1:]:
            if c in ("[", "(", "{"):
                stack.append(c)
            elif stack:
                if matches[stack.pop()] != c:
                    return False
            else:
                return False
        
        return not stack

                

            