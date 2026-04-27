def evaluate_postfix(expression):
    stack = []
    
    # Split string into tokens (e.g., "10 2 +" -> ["10", "2", "+"])
    tokens = expression.split()

    for char in tokens:
        if char.isdigit():
            # If it's a number, push to stack
            stack.append(int(char))
        else:
            # It's an operator: pop two numbers
            right = stack.pop()
            left = stack.pop()
            
            if char == '+':
                stack.append(left + right)
            elif char == '-':
                stack.append(left - right)
            elif char == '*':
                stack.append(left * right)
            elif char == '/':
                # Using // for integer division
                stack.append(left // right)
                
    return stack.pop()

expression = "5 3 2 * +"
print(f"Expression: {expression}")
print(f"Result: {evaluate_postfix(expression)}") # Output: 11