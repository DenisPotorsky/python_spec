
def check_triangle():
    a = int(input('Введите сторорону а: '))
    b = int(input('Введите сторону b: '))
    c = int(input('Введите сторону с: '))

    if a == b == c:
        print('Треугольник равносторонний')
    elif (a + b) <= c or (a + c) <= b or (b + c) <= a:
        print('Такой треугольник не существует')
    elif a == b or a == c or b == c:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')


check_triangle()