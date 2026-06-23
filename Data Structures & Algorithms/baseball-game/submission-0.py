class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for n in operations:
            if n == 'D':
                temp = int(stack[-1])
                stack.append(temp*2)
            elif n == 'C':
                stack.pop()
            elif n == '+':
                num1 = int(stack[-1])
                num2 = int(stack[-2])
                stack.append(num1+num2)
            else:
                stack.append(int(n))
        return sum(stack)