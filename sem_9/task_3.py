
import csv
from random import randint


def generate_csv():
    with open('random_nums.csv', 'w') as file:
        csv_write = csv.writer(file)
        count = randint(100, 1000)
        for i in range(count):
            csv_write.writerow([randint(10, 100), randint(10, 100), randint(10, 100)])
