class Solution:
    def isValid(self, s: str) -> bool:
        p_stack = []

        for c in s:
            if c == '(' or c == '{' or c == '[':
                p_stack.append(c)
            else:
                last = len(p_stack) - 1 
                if c == ')':
                    if p_stack and p_stack[last] == '(':
                        p_stack.pop(last)
                    else:
                        return False
                elif c == '}':
                    if p_stack and p_stack[last] == '{':
                        p_stack.pop(last)
                    else:
                        return False                   
                elif c == ']':
                    if p_stack and p_stack[last] == '[':
                        p_stack.pop(last)
                    else:
                        return False
        if p_stack:
            return False
        else:
            return True
        