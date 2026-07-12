class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-','/', '*'}
        res = 0

        if not tokens:
            return 0

        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                m = stack.pop()
                n = stack.pop()
                

                if i == "+":
                    res = n + m
                elif i == "*":
                    res = n * m
                elif i == "-":
                    res = n - m
                elif i == "/":
                    res = int(n / m)

                stack.append(int(res))

        return stack[-1]               


            
        