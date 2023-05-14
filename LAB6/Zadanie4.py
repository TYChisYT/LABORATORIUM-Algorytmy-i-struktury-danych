def oceń_wyrażenie_postfiksowe(wyrażenie):
    stos = []

    for token in wyrażenie.split():
        if token.isdigit():
            stos.append(int(token))
        else:
            operand2 =  stos.pop()
            operand1 =  stos.pop()
            result = perform_operation(token, operand1, operand2)
            stos.append(result)

    return  stos.pop()


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


wyrażenie = input("Podaj wyrażenie arytmetyczne w notacji postfiksowej: ")
result = oceń_wyrażenie_postfiksowe(wyrażenie)

print(f"Wynik wyrażenia {wyrażenie} wynosi: {result}")
