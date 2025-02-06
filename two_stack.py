"""
Dijkstra’s Two-Stack Algorithm for Expression Evaluation

This algorithm evaluates arithmetic expressions written in infix notation using two stacks:
1. **Operand Stack:** Stores numbers (operands).
2. **Operator Stack:** Stores operators (+, -, *, /).

eg: "((3 + 2) * 5)" evaluates to 25

### How It Works:
- **When encountering a number:** Push it onto the operand stack.
- **When encountering an operator:** Push it onto the operator stack.
- **When encountering a left parenthesis (`(`):** Do nothing (it just signifies precedence).
- **When encountering a right parenthesis (`)`)**:
  - Pop an operator from the operator stack.
  - Pop two operands from the operand stack.
  - Apply the operator to these two operands.
  - Push the result back onto the operand stack.
- **When expression is fully parsed:** The operand stack contains the final result.

This ensures correct evaluation based on operator precedence and parentheses.
"""


def evaluate_expression(expression: str) -> int:
    """
    Evaluate an arithmetic expression using Dijkstra’s Two-Stack Algorithm.
    
    :param expression: str - The arithmetic expression in infix notation.
    :return: int - The result of evaluating the expression.
    """
    operators = []
    operands = []
    
    def apply_operator(op: str, val2: int, val1: int) -> int:
        """Applies an operator to two operands."""
        if op == '+': return val1 + val2
        if op == '-': return val1 - val2
        if op == '*': return val1 * val2
        if op == '/': return val1 // val2  # Integer division
    
    i = 0
    while i < len(expression):
        char = expression[i]
        if char == ' ':
            i += 1
            continue
        elif char == '(':
            pass  # Do nothing for left parenthesis
        elif char.isdigit():
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            operands.append(num)
            continue
        elif char in '+-*/':
            operators.append(char)
        elif char == ')':
            op = operators.pop()
            val2 = operands.pop()
            val1 = operands.pop()
            operands.append(apply_operator(op, val2, val1))
        i += 1
    
    return operands.pop()
