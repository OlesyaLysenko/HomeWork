# Создать текстовый файл (не программно),
# сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.


def count_info():
    with open('text_2.txt', 'r', encoding="utf-8") as file:
        my_list = file.readlines()
        print(f'Количество строк: {len(my_list)}.')
        for i in range(len(my_list)):
            new_l = my_list[i].split()
            print(f' В {i + 1}-ой строке {len(new_l)} слов(а)')


count_info()
