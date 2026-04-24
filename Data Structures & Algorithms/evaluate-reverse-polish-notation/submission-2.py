class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result_stack = []

        for c in tokens:
            if c == "+":
                operand_2 = result_stack.pop()
                operand_1 = result_stack.pop()
                result = int(operand_1) + int(operand_2)
                result_stack.append(result)
            elif c == "-":
                operand_2 = result_stack.pop()
                operand_1 = result_stack.pop()
                result = int(operand_1) - int(operand_2)
                result_stack.append(result)
            elif c == "*":
                operand_2 = result_stack.pop()
                operand_1 = result_stack.pop()
                result = int(operand_1) * int(operand_2)
                result_stack.append(result)
            elif c == "/":
                operand_2 = result_stack.pop()
                operand_1 = result_stack.pop()
                result = int(float(operand_1) / float(operand_2))
                result_stack.append(result)
            else:
                result_stack.append(int(c))
        
        return result_stack.pop()