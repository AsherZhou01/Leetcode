# Time: O(n), Space: O(n)
def mark_unmatched_brackets(line):
    # To keep track of '(' positions
    stack = []
    # To mark the information of parentheses
    marks = [' '] * len(line)
    
    for i, char in enumerate(line):
        if char == '(':
            stack.append(i)  # Record the position of '('
        elif char == ')':
            if stack:
                stack.pop()
            else:
                marks[i] = '?'  # No matching '(', mark with '?'

    #  Process all unmatched '('
    for i in stack:
        marks[i] = 'x'
    
    output_line = line + '\n' + ''.join(marks)
    return output_line

# testcase
input_lines = [
    "bge)))))))))",
    "((IIII))))))",
    "()()()()(uuu",
    "))))UUUU((()",
    "abcde",  # No parentheses at all
    "(a(b)c)(d)e",  # Nested and matched parentheses
]
for line in input_lines:
    print(mark_unmatched_brackets(line))
