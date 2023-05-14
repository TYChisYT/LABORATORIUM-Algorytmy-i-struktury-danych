def evaluate_postfix_expression(expression):
    stack = []

    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = perform_operation(token, operand1, operand2)
            stack.append(result)

    return stack.pop()


def perform_operation(operator, operand1, operand2):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2
    elif operator == '^':
        return operand1 ** operand2


expression = input("Podaj wyrażenie arytmetyczne w notacji postfiksowej: ")
result = evaluate_postfix_expression(expression)

print(f"Wynik wyrażenia {expression} wynosi: {result}")
