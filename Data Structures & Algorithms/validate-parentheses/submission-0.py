class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            ')' : '(',
            '}' : '{',
            ']' : '[' 
        }
        stack = []
        for n in s:
            stack.append(n)
            if n in d:
                if len(stack) > 1 and stack[-2] == d[n]:
                    stack.pop()
                    stack.pop()
        if stack:
            return False
        return True
        

        # () [] {}
        # ( -> ) pop