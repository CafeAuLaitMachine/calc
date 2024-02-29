import re


def infix_to_postfix(fixed_exp):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []
    stack = []

    for char in fixed_exp:
        if char.replace("-", "").replace(".", "").isdigit():
            output.append(char)

        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else: # Operator
            while stack and precedence.get(stack[-1], 0) >= precedence.get(char, 0):
                output.append(stack.pop())
            stack.append(char)
    while stack:
        output.append(stack.pop())
    print(output)
    return output



def evaluate_postfix(postfix):
    stack = []
    for token in postfix:
        print(postfix)
        if token.replace("-", "").replace(".", "").isdigit():
            stack.append(float(token))
        else:
            print(stack)
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                print(operand1, "+", operand2)
                stack.append(operand1 + operand2)
            elif token == '-':
                print(operand1, "-", operand2)
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
                print(operand1, "*", operand2)
            elif token == '/':
                stack.append(operand1 / operand2)
                print(operand1, "/", operand2)
            elif token == '^':
                stack.append(operand1 ** operand2)
                print(operand1, "**", operand2)

    return stack[0]
