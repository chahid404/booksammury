import csv
import random

file = r'data/top books.csv'


def read_file(file):
    data = []
    with open(file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
        return data

def books():
    books_list = read_file(file)
    return random.choice(books_list)