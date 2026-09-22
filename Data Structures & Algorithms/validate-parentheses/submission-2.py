class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()

        mapping = {'[' : ']', '{' : '}', '(': ')'}
        
        for char in s:

            if char in mapping:
                stack.append(char)

            elif char in mapping.values():
                if not stack or mapping[stack.pop()] != char:
                    return False
            else:
                return True
        return not stack

