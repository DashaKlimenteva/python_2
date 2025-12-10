import csv
import random
import xml.etree.ElementTree as ET

MIN_SYMB = 30
with open('books-en.csv', encoding='cp1251') as file:
    reader = list(csv.DictReader(file, delimiter=';'))

#Task 1
def task_1():
    count = sum(len(row["Book-Title"]) > MIN_SYMB for row in reader)
    return count

#Task 2
def task_2(author, extra):
    with open('books-en.csv', encoding='cp1251') as file:
        result = []
        for row in reader:
            if row['Book-Author'] == author and float(row['Price'].replace(',', '.')) > extra:
                result.append(row['Book-Title'])
        return result

#Task 3
def task_3():
    randbi = random.sample(reader, 20)
    with open("bibliography.txt", "w", encoding="utf-8") as file:
        for i, b in enumerate(randbi, start=1):
            file.write(f"{i}. {b['Book-Author']}. {b['Book-Title']} - {b['Year-Of-Publication']}\n")

#Task 4
def task_4():
    tree = ET.parse('currency.xml')
    root = tree.getroot()
    values = []
    for val in root.findall('Valute'):
        value_text = val.find('Value').text
        value_float = float(value_text.replace(',', '.'))
        values.append(value_float)
    return sum(values) / len(values) if values else 0

def dop_1():
    publishers = set()
    for row in reader:
        publishers.add(row['Publisher'])
    return publishers

def dop_2(top=20):
    sorted_books = sorted(reader, key=lambda x: int(x['Downloads']), reverse=True)
    top_books = sorted_books[:top]

    for i, book in enumerate(top_books, 1):
        print(f"{i}. {book['Book-Title']}")


print(task_1())

print('author:')
a = input()
print(task_2(a, 150))

task_3()
print(task_4())
print(dop_1())
dop_2()