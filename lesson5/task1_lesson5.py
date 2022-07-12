# Создать программный файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

my_file = open('text_1.txt', 'w', encoding='UTF-8')
input("Введите текст. Для завершения ввода нажмите Enter\n")
my_str = ' '
while my_str:
    my_str = input('')
    my_file.writelines(f'{my_str}\n') if my_str != '' else my_file.close()