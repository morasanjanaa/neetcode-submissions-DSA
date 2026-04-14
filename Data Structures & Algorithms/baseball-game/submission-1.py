class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if stack and i == "C":
                stack.pop()
            elif i == "+" and len(stack)>=2:
                stack.append(stack[-1]+stack[-2])
            elif i == "D":
                stack.append(stack[-1]*2)
            else:
                stack.append(int(i))
        return sum(stack)


        