# вариант 6
import re
import csv

from idlelib.iomenu import encoding

# Задание 1
file_n1 = "task1-ru.txt"

with open(file_n1, 'r', encoding='utf-8') as file:
    f1 = file.read()
t = re.sub(r'\d[..]\d*', r'w.w', f1)
numbers_low_ten = re.findall(r'\b[0-9]\b', t)
print(numbers_low_ten)


# Задание 2
file_n2 = "task2.html"

with open(file_n2, 'r', encoding='utf-8') as file:
    f2 = file.read()

all_images = re.findall(r'[/]\S+\.png', f2)
print(all_images)

# Задание 3
file_n3 = "task3.txt"

with open(file_n3, 'r', encoding='utf-8') as file:
    f3 = file.read()

ID = re.findall(r' [0-9]+ ', f3)
Surnames = re.findall(r' [A-Z][a-z]+ ', f3)
Email = re.findall(r'\S+@\S+\.\w+', f3)
Date = re.findall(r' \d{4}-\d{2}-\d{2} ', f3)
Sites = re.findall(r' http\S+[^@]\.\S+ ', f3)

data = ['ID  Surname  Email  Date of registration  Site']
for i in range(len(ID)):
    data += [ID[i] + Surnames[i] + Email[i] + Date[i] + Sites[i]]


with open('itog_table.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter='\n')
    csvwriter.writerow(data)



