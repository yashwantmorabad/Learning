def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    output = []

    for char in expression:
        # 1. If alphanumeric, add to output
        if char.isalnum():
            output.append(char)
        
        # 2. If '(', push to stack
        elif char == '(':
            stack.append(char)
            
        # 3. If ')', pop until '(' is found
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop() # Remove '('
            
        # 4. If operator
        else:
            while stack and stack[-1] != '(' and \
                  precedence.get(stack[-1], 0) >= precedence.get(char, 0):
                output.append(stack.pop())
            stack.append(char)

    # Pop remaining operators
    while stack:
        output.append(stack.pop())

    return "".join(output)

# Test
expr = "a+b*(c^d-e)"
print(f"Infix: {expr}")
print(f"Postfix: {infix_to_postfix(expr)}") 
# Output: abcd^e-*+