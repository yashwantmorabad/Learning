def is_balanced(expression):
    stack = []
    # Map closing brackets to their corresponding opening brackets
    mapping = {")": "(", "}": "{", "]": "["}

    for char in expression:
        # If it's an opening bracket, push to stack
        if char in mapping.values():
            stack.append(char)
        
        # If it's a closing bracket
        elif char in mapping.keys():
            # If stack is empty OR top of stack doesn't match
            if not stack or stack.pop() != mapping[char]:
                return False
                
    # If the stack is empty, all brackets were matched
    return len(stack) == 0

# Test Cases
test_strings = ["{[()]}", "{[(])}", "{{[[(())]]}}","[[]()]"]

for s in test_strings:
    print(f"Is '{s}' balanced?\n{is_balanced(s)}")