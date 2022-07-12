# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

total_list = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
result = []
new_list = []

with open('text_4.txt', 'r+', encoding="UTF-8") as file:
    for line in file:
        n_list = line.split(" - ")
        print(n_list)
        if n_list[0] in total_list:
            word = total_list[n_list[0]]
            new_list.append(word + ' - ' + n_list[1])
    print(new_list)
