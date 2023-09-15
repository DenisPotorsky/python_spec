
def check_triangle(a, b, c):
    # a = int(input('Введите сторорону а: '))
    # b = int(input('Введите сторону b: '))
    # c = int(input('Введите сторону с: '))

    if a == b == c:
        return 'Треугольник равносторонний'
    elif (a + b) <= c or (a + c) <= b or (b + c) <= a:
        return 'Такой треугольник не существует'
    elif a == b or a == c or b == c:
        return 'Треугольник равнобедренный'
    else:
        return 'Треугольник разносторонний'
def test_triangle():
    assert check_triangle(2, 3, 6) == 'Такой треугольник не существует', False

