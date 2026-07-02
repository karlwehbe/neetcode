class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Trivial case: a single token means it's just one number, no operations to do
        if len(tokens) == 1:
            return int(tokens[0])

        number_stack = []
        operator_stack = []
        result = float("inf")  # placeholder, gets overwritten before ever being returned
        seen = 0  # tracks how many tokens have been consumed so far

        while seen < len(tokens):
            # Push numbers onto number_stack until an operator is hit,
            # then push that operator and stop (break) so it can be applied immediately
            for i in range(seen, len(tokens)):
                if tokens[i] not in ["*", "/", "+", "-"]: 
                    number_stack.append(tokens[i])
                    seen += 1
                else:
                    operator_stack.append(tokens[i])
                    seen += 1
                    break
            
            # Apply the operator to the two most recent numbers (RPN: operator follows its operands)
            op = operator_stack.pop(-1)
            num1 = number_stack.pop(-1)  # second operand (popped first, since it was pushed last)
            num2 = number_stack.pop(-1)  # first operand

            # Evaluate "num2 op num1" as a string expression, truncate toward zero via int(),
            # then push the result back as a string so it can feed into later operations
            result = str(int(eval(num2 + op + num1)))
            number_stack.append(result)

        return int(number_stack[0])
        