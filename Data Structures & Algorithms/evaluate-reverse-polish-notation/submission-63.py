class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        number_stack = []
        operator_stack = []
        result = float("inf")
        seen = 0

        while seen < len(tokens):
            print(tokens)
            for i in range(seen, len(tokens)):
                if tokens[i] not in ["*", "/", "+", "-"]: 
                    number_stack.append(tokens[i])
                    seen += 1
                else:
                    operator_stack.append(tokens[i])
                    seen += 1
                    break
                print(tokens[i], seen)
            
            print(number_stack, operator_stack)

            op = operator_stack.pop(-1)
            num1 = number_stack.pop(-1)
            num2 = number_stack.pop(-1)

            if op == "/":
                result = str(int(eval(num2 + op + num1)))
            else:
                result = str(int(eval(num2 + op + num1)))

            number_stack.append(result)
            print("___________________")

        return int(number_stack[0])
            

        