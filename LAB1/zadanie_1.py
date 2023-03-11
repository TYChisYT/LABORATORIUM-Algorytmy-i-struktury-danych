import math

a = 2
b = 16
c = 14
if a!= 0:
    delta = b * b - 4 * a * c
    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        print("wyniki ", x1, x2)
    elif delta == 0:
        x1 = -b / (2 * a)
        print('wynik ', x1)
    else:
        print('Brak rozwiązań rzeczywistych')
else:
    print('To nie jest równanie kwadratowe')
