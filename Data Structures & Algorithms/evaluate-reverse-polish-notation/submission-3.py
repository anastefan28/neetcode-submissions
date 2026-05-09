class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                term1 = stack.pop()
                term2 = stack.pop()
                print(term1, term2)
                if token == "+":
                    stack.append(term1 + term2)
                if token == "*":
                    stack.append(term1 * term2)
                if token == "-":
                    stack.append(term2 - term1)
                if token == "/":
                    stack.append(int(term2 / term1))
                print(stack[0])
        return stack[0]
                