def prime():
    INPUT_LIMIT = 100000
    while True:
        number = int(input('Введите число: '))
        if number < 1 or number > INPUT_LIMIT:
            print('Введите положительное число до 100 000!')
            continue
        counter = 0
        for i in range(1, number):
            if number % i == 0:
                counter += 1
        return 'Простое число' if counter < 2 else 'Составное число'


print(prime())
